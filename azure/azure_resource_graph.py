# export VAULT_ADDR="YOUR_VAULT_ADDRESS"
# export SECRET_PATH="secret/data/azure-spn"
# export AZURE_TENANT_ID="YOUR_TENANT_ID"
# export AZURE_CLIENT_ID="YOUR_SPN_APP_ID"
# export AZURE_SUBSCRIPTION_ID="YOUR_SUBSCRIPTION_ID"

import hvac
import os
from azure.identity import ClientSecretCredential
from azure.mgmt.resourcegraph import ResourceGraphClient
from azure.mgmt.resourcegraph.models import QueryRequestOptions, QueryRequest
import json

# --- 1. Fetch the SPN password (client secret) from HashiCorp Vault ---

# Configure Vault access (adjust as needed for your Vault setup)
# Ensure VAULT_ADDR and VAULT_TOKEN environment variables are set
vault_addr = os.environ.get("VAULT_ADDR", "http://127.0.0.1:8200") # Replace with your Vault address
vault_token = os.environ.get("VAULT_TOKEN") # Use a valid Vault token with access to the secret path
secret_path = "azure/credentials/your-role-name" # Path to your Azure secret in Vault

if not vault_token:
    raise ValueError("VAULT_TOKEN environment variable not set")

try:
    client = hvac.Client(url=vault_addr, token=vault_token)
    if not client.is_authenticated():
        raise hvac.exceptions.VaultPermissionDenied("Failed to authenticate to Vault")
    
    # Retrieve the secret
    read_response = client.read(secret_path)
    if not read_response or not read_response.get('data'):
        raise Exception(f"Secret not found at path: {secret_path}")

    # The actual secret value is typically within 'data' -> 'client_secret' (depending on configuration)
    spn_client_secret = read_response['data']['client_secret'] 
    print("Successfully fetched client secret from Vault.")

except Exception as e:
    print(f"Error fetching secret from Vault: {e}")
    exit()

# --- 2. Authenticate to Azure using the Service Principal credentials ---

# Get the other SPN details from environment variables
spn_client_id = os.environ.get("AZURE_CLIENT_ID")
spn_tenant_id = os.environ.get("AZURE_TENANT_ID")
azure_subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID") # Used for the query scope

if not all([spn_client_id, spn_tenant_id, azure_subscription_id]):
    raise ValueError("AZURE_CLIENT_ID, AZURE_TENANT_ID, and AZURE_SUBSCRIPTION_ID environment variables must be set.")

# Create the credential object using the client secret from Vault
credential = ClientSecretCredential(
    tenant_id=spn_tenant_id,
    client_id=spn_client_id,
    client_secret=spn_client_secret
)
print("Azure credential object created.")

# --- 3. Run an Azure Resource Graph query ---

# Create an Azure Resource Graph client
arg_client = ResourceGraphClient(credential)

# Define your Resource Graph query
# This example query lists all virtual machines
query_string = "Resources | where type =~ 'microsoft.compute/virtualmachines' | project name, location, resourceGroup, tags"

# Define query options (scope, result format, etc.)
query_options = QueryRequestOptions(result_format="objectArray")

# Define the query request with the subscription ID scope
query_request = QueryRequest(
    subscriptions=[azure_subscription_id],
    query=query_string,
    options=query_options
)

# Execute the query
try:
    response = arg_client.resources(query_request)
    print(f"Query executed successfully. Found {len(response.data)} resources.")
    # Print results in a readable format
    print(json.dumps(response.data, indent=2))
except Exception as e:
    print(f"Error running Azure Resource Graph query: {e}")
