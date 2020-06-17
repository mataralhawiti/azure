# https://docs.microsoft.com/en-us/azure/cosmos-db/table-storage-how-to-use-python
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


"""
TableService(account_name=None, account_key=None, sas_token=None, is_emulated=False, protocol='https', endpoint_suffix='core.windows.net', request_session=None, connection_string=None, socket_timeout=None)
"""
# using account key
#table_service = TableService(account_name='myaccount', account_key='mykey')


# using sas_token
# remove ?
table_service = TableService(account_name='xxxxxx', sas_token='sv=2019-10-10&xxxxx')

#table_service.list_tables()

# check if a table exists
print(table_service.exists('xxTablenamexx', timeout=None))