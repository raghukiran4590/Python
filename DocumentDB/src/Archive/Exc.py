import cx_Oracle
import pandas as pd

oracle_dsn = cx_Oracle.makedsn("dc04px21-scan1.internal.das", 1525, service_name="topoprd")   #Prod
conn_oracle = cx_Oracle.connect(user='wdbs', password='YBkHzLmvsQG-n3rTUOpCdAfW$', dsn=oracle_dsn)
cursor = conn_oracle.cursor()
#cursor.callproc("wdbs.job_pck.start_execution", ['COLLECT_DOCDB_ALL_DATA_N'])
cursor.callproc("wdbs.job_pck.end_job_success",['COLLECT_DOCDB_ALL_DATA_N',0])
conn_oracle.commit()
conn_oracle.close()
print('done')
