import json
from datetime import datetime, time
from os import name
from urllib import response
from wsgiref import headers
import requests
import logging
import asyncio

logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO
)

timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
# sn_dbinfo_user = "srcInfoHubAPI"
# sn_dbinfo_pass = "rv0qEg&3fpY82Evp"
sn_dbinfo_user = "AF35861"
sn_dbinfo_pass = "TampaBay@123"
sn_auth_dod = (sn_dbinfo_user, sn_dbinfo_pass)
servicenow_azure_managed_instances_payload = []
servicenow_azure_managed_databases_payload = []
servicenow_azure_sqlservers_payload = []
servicenow_azure_sqlservers_databases_payload = []
url = 'https://elevancehealthdev.service-now.com/api/now/import/x_weoi2_cld_db_imp_azure_cloud_data_load/insertMultiple'

logging.info("Processing Azure SQL Managed Instances data...")
# logging.info("Timestamp for this run:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def post_to_servicenow(url, data, name, auth):
    if not data:
        return f"No data to post for {name}"
    try:
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        response = requests.post(url, headers=headers, auth=auth, json={"results": data}, verify=False)
        status = f"Successfully posted {name}" if response.status_code in [200, 201] else f"Failed to post {name}"
        logging.info(f"Posted {name} - {status} ({response.status_code})")
        data = response.json() if response.status_code in [200, 201] else response.text
        return f"Posted {name} with status code {response.status_code} and response: \n {data}"
    except Exception as e:
        logging.error(f"Failed to post {name}: {e}")
        return f"Error posting {name}: {e}"
    
def post_to_snow_azure_table(name, auth):
    try:
        with open('./azure_resource_data_2026_03_25/azure_sql_managed_instance.json', 'r') as file:
            data = json.load(file)
        
        url = 'https://elevancehealthdev.service-now.com/api/now/import/x_weoi2_cld_db_imp_azure_cloud_data_load/insertMultiple'
        headers = {"Content-Type":"application/json","Accept":"application/json"}
        response = requests.post(url, headers=headers, auth=auth, json={"results": data}, verify=False)
        status = f"Successfully posted {name}" if response.status_code in [200, 201] else f"Failed to post {name}"
        logging.info(f"Posted {name} - {status} ({response.status_code})")
        result = response.json() if response.status_code in [200, 201] else response.text
        return f"Posted {name} with status code {response.status_code} and response: \n {result}"
    except Exception as e:
        logging.error(f"Failed to post {name}: {e.__str__()}")
        return f"Error posting {name}: {e}"

async def extract_sql_managed_instances():
    logging.info(f"Started processing SQL Managed Instances")
    try:
        with open('./azure_resource_data_2026_03_25/azure_json_files/SQLManagedInstances_2026_03_25.json', 'r') as file:
            data = json.load(file)
            # for item in data:
            #     logging.info(f"Object ID: {item['id']}")

            servicenow_azure_managed_instances_payload.extend([
                        {
                            # "u_capture_dttm": timestamp,
                            "u_id": item['id'],
                            "u_name": item['name'],
                            "u_type": item['type'],
                            "u_location": item['location'],
                            "u_resourcegroup": item['resourceGroup'],
                            "u_subscriptionid": item['subscriptionId'],
                            "u_fullyqualifieddomainname": item['properties']['fullyQualifiedDomainName'],
                            "u_tenantid": item['tenantId'],
                            "u_kind": item['kind']
                            # "environment": item['tags']['environment'] if 'environment' in item['tags'] else "N/A",
                            # "elvh-app-servicenow-group": item['tags']['elvh-app-servicenow-group'] if 'elvh-app-servicenow-group' in item['tags'] else "N/A",
                            # "elvh-application-name" : item['tags']['elvh-application-name'] if 'elvh-application-name' in item['tags'] else "N/A"
                        }
                        for item in data
            ])
        logging.info(f"Finished processing SQL Managed Instances")
        print(servicenow_azure_managed_instances_payload)
        return "Servicenow Azure SQL Managed Instances payload processing complete"
    except Exception as e:
        logging.error(f"Error processing SQL Managed Instances: {e}")
        return f"Error processing SQL Managed Instances: {e}"
    
async def extract_sql_managed_databases():
    logging.info(f"Started processing SQL Managed Databases")
    with open('./azure_resource_data_2026_03_09/azure_json_files/SQLManagedDatabases_2026_03_09.json', 'r') as file:
        data = json.load(file)
        # for item in data:
        #     logging.info(f"Object ID: {item['id']}")

        servicenow_azure_managed_databases_payload.extend([
                    {
                        "u_capture_dttm": timestamp,
                        "object_id": item['id'],
                        "name": item['name'],
                        "type": item['type'],
                        "location": item['location'],
                        "u_resource_group": item['resourceGroup'],
                        "u_subscription_id": item['subscriptionId'],
                        "fullyQualifiedDomainName": item['properties']['fullyQualifiedDomainName'],
                        "environment": item['tags']['environment'] if 'environment' in item['tags'] else "N/A",
                        "elvh-app-servicenow-group": item['tags']['elvh-app-servicenow-group'] if 'elvh-app-servicenow-group' in item['tags'] else "N/A",
                        "elvh-application-name" : item['tags']['elvh-application-name'] if 'elvh-application-name' in item['tags'] else "N/A"
                    }
                    for item in data
        ])
    logging.info(f"Finished processing SQL Managed Databases")
    return "Servicenow Azure SQL Managed Databases payload processing complete"

async def extract_sql_servers():
    logging.info(f"Started processing SQL Servers")
    with open('./azure_resource_data_2026_03_09/azure_json_files/SQLServers_2026_03_09.json', 'r') as file:
        data = json.load(file)
        # for item in data:
        #     print(f"Object ID: {item['id']}")

        servicenow_azure_sqlservers_payload.extend([
                    {
                        "u_capture_dttm": timestamp,
                        "object_id": item['id'],
                        "name": item['name'],
                        "type": item['type'],
                        "location": item['location'],
                        "u_resource_group": item['resourceGroup'],
                        "u_subscription_id": item['subscriptionId'],
                        "fullyQualifiedDomainName": item['properties']['fullyQualifiedDomainName'],
                        "environment": item['tags']['environment'] if 'environment' in item['tags'] else "N/A",
                        "elvh-app-servicenow-group": item['tags']['elvh-app-servicenow-group'] if 'elvh-app-servicenow-group' in item['tags'] else "N/A",
                        "elvh-application-name" : item['tags']['elvh-application-name'] if 'elvh-application-name' in item['tags'] else "N/A"
                    }
                    for item in data
        ])
    logging.info(f"Finished processing SQL Servers")
    return "Servicenow Azure SQL Servers payload processing complete"

async def extract_sql_servers_databases():
    logging.info(f"Started processing SQL Servers Databases")
    with open('./azure_resource_data_2026_03_09/azure_json_files/SQLServerDatabases_2026_03_09.json', 'r') as file:
        data = json.load(file)
        # for item in data:
        #     print(f"Object ID: {item['id']}")

        servicenow_azure_sqlservers_databases_payload.extend([
                    {
                        "u_capture_dttm": timestamp,
                        "object_id": item['id'],
                        "name": item['name'],
                        "type": item['type'],
                        "location": item['location'],
                        "u_resource_group": item['resourceGroup'],
                        "u_subscription_id": item['subscriptionId'],
                        "fullyQualifiedDomainName": item['properties']['fullyQualifiedDomainName'],
                        "environment": item['tags']['environment'] if 'environment' in item['tags'] else "N/A",
                        "elvh-app-servicenow-group": item['tags']['elvh-app-servicenow-group'] if 'elvh-app-servicenow-group' in item['tags'] else "N/A",
                        "elvh-application-name" : item['tags']['elvh-application-name'] if 'elvh-application-name' in item['tags'] else "N/A"
                    }
                    for item in data
        ])
    logging.info(f"Finished processing SQL Servers Databases")
    return "Servicenow Azure SQL Servers Databases payload processing complete"

async def extract():
    results = await asyncio.gather(
        extract_sql_managed_instances(),
        # extract_sql_managed_databases(),
        # extract_sql_servers(),
        # extract_sql_servers_databases()
    )
    logging.info(f"All extraction functions complete. Results: {results}")

def load():
    post_to_servicenow(url, servicenow_azure_managed_instances_payload, "ServiceNow Azure SQL Managed Instances", sn_auth_dod),
    time.sleep(5)
    # post_to_servicenow(url, servicenow_azure_managed_databases_payload, "ServiceNow Azure SQL Managed Databases", sn_auth_dod),
    # time.sleep(5)
    # post_to_servicenow(url, servicenow_azure_sqlservers_payload, "ServiceNow Azure SQL Servers", sn_auth_dod),
    # time.sleep(5)
    # post_to_servicenow(url, servicenow_azure_sqlservers_databases_payload, "ServiceNow Azure SQL Servers Databases", sn_auth_dod)
    # time.sleep(5)
    logging.info(f"All load functions complete.")

async def main():
    await extract()
    await asyncio.sleep(5)  # Ensure all extraction is fully complete before loading
    # await load()
    # await asyncio.sleep(5)  # Ensure all loading is fully complete before finishing
    logging.info(f"All tasks complete.")

if __name__ == "__main__":
    # asyncio.run(main())
    post_to_snow_azure_table("ServiceNow Azure SQL Managed Instances", sn_auth_dod)

