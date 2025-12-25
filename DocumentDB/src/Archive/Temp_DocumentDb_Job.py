#---------------------------- NON PROD (Dev) Tables and SNOW DEV API -----------------------------
import os
import pandas as pd
import pyodbc
import cx_Oracle
from pymongo import MongoClient
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from threading import Lock
import warnings
import requests
import time
import logging
from dotenv import load_dotenv
import json
import sys

print('yes')
try:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    config_file = current_dir + '\\conf'
    certificates = config_file + '\\certificates'
    log_dir = current_dir + '\\logs'
    ssl_cert = certificates + '\\global-bundle 1.pem'
    env_path = config_file + '\\creds\\cred.env'
    query_location=config_file+'\\query'
    query_loc=query_location+'\\Queries.txt'
    print('came')
    #-----------------------Set up log directory-----------------------
    os.makedirs(log_dir, exist_ok=True)

    # Generate timestamp-based log filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"documentdb_log_{timestamp}.log"
    log_file = os.path.join(log_dir, log_filename)

    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s [%(levelname)s] %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    # Get logger
    logger = logging.getLogger(__name__)
    #-------------------------------------------------------------------

    #-----------------------#Reading Creds-------------------------------

    load_dotenv(dotenv_path=env_path)

    # Check if path was loaded
    if not os.path.exists(env_path):
        logging.info(f"[ERROR] .env file not found at: {env_path}")
    else:
        logging.info(f"[INFO] Loaded All credentials from .env file: {env_path}")

    # Read credentials
    mongo_user = os.getenv("MONGO_USER")
    mongo_pass = os.getenv("MONGO_PASS")
    sn_dod_user = os.getenv("SN_DOD_USER")
    sn_dod_pass = os.getenv("SN_DOD_PASS")
    sn_dod_pass_dev = os.getenv("SN_DOD_PASS_DEV")
    sn_dbinfo_user = os.getenv("SN_DBINFO_USER")
    sn_dbinfo_pass = os.getenv("SN_DBINFO_PASS")
    sn_dbinfo_pass_dev=os.getenv("SN_DBINFO_PASS_DEV")
    oracle_user = os.getenv("ORACLE_USER")
    oracle_pass = os.getenv("ORACLE_PASS")
    print(oracle_user)
    #---------------------------------------------------------------------

    #-------------- ServiceNow POST Request Creds Intailaizing (Prod Data)------------
    sn_auth_dod = (sn_dod_user, sn_dod_pass_dev)
    sn_auth_dbinfo = (sn_dbinfo_user, sn_dbinfo_pass_dev)
    #---------------------------------------------------------------------

    warnings.filterwarnings('ignore')
    print('Starting...', datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    #log starts

    #----------------Supporting Lists for Itterations -----------------------
    report_data = []
    dbids_data = []
    avatar_data = []
    servicenow_db_payload = []
    servicenow_info_payload = []
    lock = Lock()
    logging.info("=== Supporting Itteration List for Data Processing were Initialized ===")

    # ---------- Oracle Cursor Part ------------------------
    #oracle_dsn = cx_Oracle.makedsn("va33dx14-scan1.wellpoint.com", 1525, service_name="topod")   #Dev
    #oracle_dsn = cx_Oracle.makedsn("dc04px21-scan1.internal.das", 1525, service_name="topoprd")   #Prod
    oracle_dsn = cx_Oracle.makedsn("ihubtopo-d-01.internal.das", 1525, service_name="topod")    #OCI
    conn_oracle = cx_Oracle.connect(user=oracle_user, password=oracle_pass, dsn=oracle_dsn)
    cursor = conn_oracle.cursor()

    # ------- Inventory which we need to try connection Everyday ---------

    prod_ind_bat = sys.argv[1] #reading Env from Bat file
    
    with open(query_loc, 'r') as f:
        oracle_query = f.read()
    #oracle_query+=prod_ind_bat
    #print(oracle_query)
    df_oracle = pd.read_sql(oracle_query, con=conn_oracle)
    df_oracle.columns = df_oracle.columns.str.strip().str.lower()
    df_oracle[['con_str', 'port']] = df_oracle['connection_string'].str.split(':', expand=True)
    df = df_oracle
    print(len(df))
    df=df[df['prod_ind']==prod_ind_bat]
    logging.info(f"Total MongoDB instances to connect: {len(df)}")

    #-------- Start Packages Executions ----------------
    prod_ind=df['prod_ind'].iloc[0]
    if prod_ind=='N':
        logging.info("=== DocumentDB Python Collectors for Non Prod Started ===")
    else:
        logging.info("=== DocumentDB Python Collectors for Prod Started ===")

    packages = ['COLLECT_DOCDB_ALL_DATA_', 'COLLECT_DOCDB_DATABASES_', 'COLLECT_DOCDB_DBINFO_']
    jobname=[]
    jobname=[i + prod_ind for i in packages]
    for pkg in jobname:
        try:
            cursor.callproc("wdbs.job_pck.start_execution", [pkg])
            logging.info(f"Started job package: {pkg}")
            time.sleep(1)
        except Exception as e:
            logging.error(f"Failed to start package {pkg}: {e}")

    conn_oracle.commit()

    # --- MongoDB Processing Function ---
    def check_mongo_connection(index, row):
        uri = (
            f"mongodb://{mongo_user}:{mongo_pass}@{row['con_str']}:{row['port']}/"
            f"?tls=true&tlsCAFile={ssl_cert}&retryWrites=false"
        )
        try:
            client = MongoClient(uri, serverSelectionTimeoutMS=30000,
                                connectTimeoutMS=30000, socketTimeoutMS=30000)
            build_info = client.admin.command("buildinfo")
            users_info = client.admin.command("usersInfo")
            databases = client.list_database_names()
            capture_dttm = datetime.now().strftime('%d-%b-%y').upper()
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            logging.info(f"[{index}] Connected to {row['server_nm']} - Version: {build_info.get('version', '')}, Databases: {len(databases)}, Users: {len(users_info.get('users', []))}")
            with lock:
                dbids_data.extend([
                    (
                        capture_dttm, row['dbms_type'], row['server_nm'], row['instance_nm'],
                        user['user'], 'ACTIVE', 'SERVICE ID', row['sys_id'], int(row['instance_key'])
                    )
                    for user in users_info.get('users', [])
                ])
                avatar_data.extend([
                    (
                        capture_dttm, role['db'], user['user'], row['sys_id'],
                        role['role'], int(row['instance_key'])
                    )
                    for user in users_info.get('users', [])
                    for role in user.get('roles', [])
                ])
                servicenow_db_payload.extend([
                    {
                        "u_capture_dttm": timestamp,
                        "u_db_type": "DOCUMENTDB",
                        "u_instance_sys_id": row['sys_id'],
                        "u_database_name": db,
                        "u_production_ind": row['prod_ind']
                    }
                    for db in databases
                ])
                servicenow_info_payload.append({
                    "u_instance_sys_id": row['sys_id'],
                    "u_db_type": "DOCUMENTDB",
                    "u_db_version": build_info.get('version', '')
                })
                #if you want failure report in any situation below use below one
                report_data.append({
                    'sys_id': row['sys_id'],
                    'ConnectionString': row['con_str'],
                    'Connection status': 'Pass',
                    'Reason for failure': ''
                })

        except Exception as e:
            logging.error(f"[{index}] ERROR connecting to {row['server_nm']} - {e}")
            cursor.callproc("wdbs.connection_pck.add_error_message", [
                int(row['instance_key']), row['instance_nm'], row['sys_id'],
                jobname[0], str(e), row['con_str'], mongo_user
            ])
            conn_oracle.commit()
            with lock:
                report_data.append({
                    'sys_id': row['sys_id'],
                    'ConnectionString': row['con_str'],
                    'Connection status': 'Fail',
                    'Reason for failure': str(e)
                })
            return (index, 'Failed', str(e))
        finally:
            if 'client' in locals():
                client.close()

    # --- Threaded Mongo Connections ---
    with ThreadPoolExecutor(max_workers=4) as executor:
        futures = [executor.submit(check_mongo_connection, i, df.loc[i]) for i in range(len(df))]
        for future in as_completed(futures):
            try:
                future.result()
            except Exception as e:
                logging.error(f"Thread Exception Occured {e}")
    # ------------------------- Oracle Inserts -----------------------------------
    conn_oracle_1 = cx_Oracle.connect(user=oracle_user, password=oracle_pass, dsn=oracle_dsn)
    cursor_1 = conn_oracle_1.cursor()

    if dbids_data:
        cursor.executemany("""
            INSERT INTO WDBS.STAGE_DBIDS_DOCUMENTDB 
            (CAPTURE_DTTM, DBMS_TYPE, HOST, INSTANCE_NM, LOGINID, IDSTATUS, DBID_TYPE_NM, INSTANCE_SYS_ID, INSTANCE_KEY)
            VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)
        """, dbids_data)
        logging.info(f"Inserted {len(dbids_data)} DBIDS records.")

    if avatar_data:
        cursor.executemany("""
            INSERT INTO WDBS.STAGE_AVATAR_DOCUMENTDB_ID_PRIVS 
            (CAPTURE_DTTM, DATABASE_NM, LOGIN_ID, INSTANCE_SYS_ID, ROLE_NAME, INSTANCE_KEY)
            VALUES (:1, :2, :3, :4, :5, :6)
        """, avatar_data)
        logging.info(f"Inserted {len(avatar_data)} Avatar records.")


    conn_oracle_1.commit()
    cursor_1.close()
    conn_oracle_1.close()

    logging.info(f"Data Insertions to Stage Tables were successfull and Cursor Closed")

    # --- ServiceNow Posting ---
    headers = {"Content-Type": "application/json"}

    def post_to_servicenow(url, data, name, auth,size,package):
        if not data:
            return 204
        try:
            response = requests.post(url, headers=headers, auth=auth, json={"records": data}, verify=False)
            status = "Success" if response.status_code in [200, 201] else "Failed"
            logging.info(f"Posted {name} - {status} ({response.status_code})")
            return response.status_code
        except Exception as e:
            logging.error(f"Failed to post {name}: {e}")
            

    # --- Final Job Completion Tracking ---
    job_failures = []
    job_warnings = []
    time.sleep(2)
    try:
        logging.info("ServiceNow DOD PUSH STARTED")
        status_code = post_to_servicenow(
            "https://elevancehealthdev.service-now.com/api/now/import/u_infohub_database_import/insertMultiple",
            servicenow_db_payload, "ServiceNow DOD", sn_auth_dod,len(servicenow_db_payload),jobname[1]
        )
        if status_code not in [200, 201]:
            job_warnings.append((jobname[1], len(servicenow_db_payload)))
            cursor.callproc("wdbs.job_pck.END_JOB_COMPLETE_WITH_WARNING",[jobname[1], len(servicenow_db_payload)])
            logging.info(f"{jobname[1]} Job Completed with Warnings")
        else:
            cursor.callproc("wdbs.job_pck.end_job_success",[jobname[1], len(servicenow_db_payload)])
            logging.info(f"{jobname[1]} Job Completed Successfull")
                        
    except Exception as e:
        job_failures.append((jobname[1], str(e)))
        cursor.callproc("wdbs.job_pck.end_job_failure", [jobname[1], str(e), 0])
        logging.info(f"{jobname[1]} Job Failed --> {e}")
        
    time.sleep(2)
    try:
        logging.info("ServiceNow DbInfo PUSH STARTED")
        status_code = post_to_servicenow(
            "https://elevancehealthdev.service-now.com/api/now/import/u_infohub_dbinfo_import/insertMultiple",
            servicenow_info_payload, "ServiceNow DbInfo", sn_auth_dbinfo,len(servicenow_info_payload),jobname[2]
        )
        if status_code not in [200, 201]:
            job_warnings.append((jobname[2], len(servicenow_info_payload)))
            cursor.callproc("wdbs.job_pck.END_JOB_COMPLETE_WITH_WARNING",[jobname[2], len(servicenow_info_payload)])
            logging.info(f"{jobname[2]} Job Completed with Warnings")
        else:
            cursor.callproc("wdbs.job_pck.end_job_success",[jobname[2], len(servicenow_info_payload)])
            
    except Exception as e:
        job_failures.append((jobname[2], str(e)))
        cursor.callproc("wdbs.job_pck.end_job_failure", [jobname[2], str(e), 0])
        logging.info(f"{jobname[2]} Job Failed --> {e}")
        
    time.sleep(2)
    # --- Main Job Completion ---
    if job_failures:
        for job, err in job_failures:
            cursor.callproc("wdbs.job_pck.end_job_failure", [jobname[0], err, 0])
            logging.info(f"{jobname[0]} Job Failed Because DOD or DBInfo Failed")
    else:
        cursor.callproc("wdbs.job_pck.end_job_success", [jobname[0], len(df)])
        logging.info("All Job Ran Successfully")
        
    time.sleep(2)
    conn_oracle.commit()
    cursor.close()
    conn_oracle.close()
    # --- Report ---                        if you want failure as report get from this.
    #report_df = pd.DataFrame(report_data)
    #output_file = r'C:\Users\AL20098\Documents\DocumentDb_Python_Job\SupportFiles\Mongo_Connection_Report.xlsx'
    #report_df.to_excel(output_file, index=False)
    #print(f"\nMongoDB connection report saved to: {output_file}")


    #-------------------------------- Email Sending part -----------------------

    url = "https://emep-services.anthem.com/misc/utilityfaxnmail/members/JKJKJDS8989389383/email-utility"
    headers = {"Content-Type": "application/json"}
    body = {
        'staticData': {
            'fromEmail': 'noreply@anthem.com',
            'toEmail': ['muralitharan.s@carelon.com'],
            #'ccEmail': ['raghu.kiran@elevancehealth.com'],
            'subject': f'DocumentDB NON PROD Data Load SUCCESFULL',
            'body': {'content': f"Today's Load Completed In Non Prod <br><br>Thanks", 'bodyContentType': 'HTML', 'toMarkSecure': 'true'}
        }
        #,
        # 'dynamicData': {
        #     'inLineResource': [{
        #         'data': {'content': 'test,test2,tes3\n,tes4,tes5,test6', 'filetype': 'txt', 'encoding': 'none'},
        #         'inLineResourceID': 'Deployment Details Report',
        #         'archiveResource': 'none'
        #     }]
        # }
    }
    response = requests.request("POST", url, data=json.dumps(body), headers=headers, verify=False)
    if response.status_code == 200:
        logging.info("Email sent successfully")
    else:
        logging.info(f"Failed to send email: {response.reason}")
except Exception as e:
    logging.info(f"Exception Occured: {e}")
