# export AZURE_CLIENT_ID = <Application (client) ID>
# export AZURE_TENANT_ID = <Directory (tenant) ID>
# export AZURE_CLIENT_SECRET = <Client secret value> 
# export AZURE_SUBSCRIPTION_ID = <subscription ID> 

import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient

# The DefaultAzureCredential will automatically use the environment variables
# AZURE_CLIENT_ID, AZURE_TENANT_ID, and AZURE_CLIENT_SECRET
try:
    credential = DefaultAzureCredential()

    # Example of using the credential to manage resources (replace with your specific service client)
    # You'll need your Azure Subscription ID for this example
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID", "<your-subscription-id>")
    resource_client = ResourceManagementClient(credential, subscription_id)

    print("Successfully authenticated with Azure using Service Principal.")

    # Example: List resource groups (uncomment to test)
    # for group in resource_client.resource_groups.list():
    #     print(f"Resource Group: {group.name}")

except Exception as e:
    print(f"Authentication failed: {e}")
