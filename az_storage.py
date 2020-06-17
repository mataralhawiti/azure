
"""
Client Packages:
    - azure-storage-blob (https://azuresdkdocs.blob.core.windows.net/$web/python/azure-storage-blob/12.0.0/index.html)
    - azure-storage-file-datalake
    - azure-storage-file-share
    - azure-storage-queue


Management Packages:
    - azure-mgmt-storage
    - azure-mgmt-storagecache
"""
import configparser

config = configparser.ConfigParser()
config.read('config.cfg')

AZURE_CLIENT_ID = config.get("CREDENTIALS","AZURE_CLIENT_ID")
AZURE_CLIENT_SECRET = config.get("CREDENTIALS","AZURE_CLIENT_SECRET")
AZURE_TENANT_ID = config.get("CREDENTIALS","AZURE_TENANT_ID")
AZURE_SUBSCRIPTION_ID = config.get("CREDENTIALS","AZURE_SUBSCRIPTION_ID")

GROUP_NAME = "rg_playground"
STORAGE_ACCOUNT_NAME = "invalid-or-used-name"

# set our credentials
from azure.common.credentials import ServicePrincipalCredentials
credentials = ServicePrincipalCredentials(
    client_id = AZURE_CLIENT_ID,
    secret = AZURE_CLIENT_SECRET,
    tenant = AZURE_TENANT_ID
)

# get resource client
# from azure.mgmt.resource import ResourceManagementClient
# client_resource = ResourceManagementClient(credentials, AZURE_SUBSCRIPTION_ID)
# print(client_resource)

# get storage client
from azure.mgmt.storage import StorageManagementClient
storage_client = StorageManagementClient(credentials, AZURE_SUBSCRIPTION_ID)


# https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5
def is_valid_name(storage_client : str, storage_acct_name : str) -> bool :
    """
    Check if the storage account name is avialable
    """
    availability = storage_client.storage_accounts.check_name_availability(storage_acct_name).name_available
    return availability



# let's test
check_name = is_valid_name(storage_client, STORAGE_ACCOUNT_NAME)
print(check_name)