import datetime
import sys
import os
# here we add 3rd party module, and this how it's done on Azure functions
#sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'yourenv/Lib/site-packages')))
import requests
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

# grap the param frm the received request 
# links = os.environ['req_query_links']
# print(links)


links = ['https://api.dowjones.com/alpha/extractions/stream?file=dj-xxxxxx/part-00000-of-00025.avro', 'https://api.dowjones.com/alpha/extractions/stream?file=dj-7596b4a8a24903cbd83a28d5c8b4a2b1/format=avro/extraction/dj-synhub-extraction-7596b4a8a24903cbd83a28d5c8b4a2b1-u2tknbtqhk/part-00001-of-00025.avro']

BLOCK_BLOB_SERVICE = BlockBlobService(account_name='mediascan', 
                                        account_key='xxxx')
BLOB_CONTAINER_AVRO = 'test-avro'

headers = {'content-type': 'application/json', 'user-key': 'xx'}

for link in links :
    try:
        file_name = str(datetime.date.today().strftime("%Y%m%d")) +'_'+str(link.split('/')[-1])
        r = requests.get(link, stream=True, headers=headers)
        BLOCK_BLOB_SERVICE.create_blob_from_bytes(
        BLOB_CONTAINER_AVRO,
        file_name,
        r.content
                )
        print("done uploading  "+str(link.split('/')[-1]) + " to Azure Blob")
    except requests.exceptions.RequestException as e:
        print('exception caught', e)
print("... Done uploading all files to Azure Blob [ " + BLOB_CONTAINER_AVRO + " ]... \n\n")




try:
    file_name = str(datetime.date.today().strftime("%Y%m%d")) +'_'+str(link.split('/')[-1])
    r = requests.get(link, stream=True, headers=headers)
    BLOCK_BLOB_SERVICE.create_blob_from_bytes(
    BLOB_CONTAINER_AVRO,
    file_name,
    r.content
            )
    print("done uploading  "+str(link.split('/')[-1]) + " to Azure Blob")
except requests.exceptions.RequestException as e:
    print('exception caught', e)

print("... Done uploading all files to Azure Blob [ " + BLOB_CONTAINER_AVRO + " ]... \n\n")




import datetime
import sys
import os
import json

# here we add 3rd party module, and this how it's done on Azure functions
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), 'yourenv/Lib/site-packages')))
import requests
from azure.storage.blob import BlockBlobService
from azure.storage.blob import ContentSettings

# grap the param frm the received request 
links = os.environ['req_query_links']
print(links)

output = open(os.environ['res'], 'w')
output.write(json.dumps(link))


BLOCK_BLOB_SERVICE = BlockBlobService(account_name='mediascan', 
                                        account_key='x/xx+xx==')
BLOB_CONTAINER_AVRO = 'test-avro'

headers = {'content-type': 'application/json', 'user-key': 'xxxxxx'}


for link in links :
    try:
        file_name = str(datetime.date.today().strftime("%Y%m%d")) +'_'+str(link.split('/')[-1])
        r = requests.get(link, stream=True, headers=headers)
        BLOCK_BLOB_SERVICE.create_blob_from_bytes(
        BLOB_CONTAINER_AVRO,
        file_name,
        r.content
                )
        print("done uploading  "+str(link.split('/')[-1]) + " to Azure Blob")
    except requests.exceptions.RequestException as e:
        print('exception caught', e)
print("... Done uploading all files to Azure Blob [ " + BLOB_CONTAINER_AVRO + " ]... \n\n")


#output = open(os.environ['res'], 'w')
#output.write(json.dumps(link))


"""
https://stackoverflow.com/questions/24535920/difference-between-data-and-params-in-python-requests
https://stackoverflow.com/questions/2602043/rest-api-best-practice-how-to-accept-list-of-parameter-values-as-input
https://github.com/Azure/azure-functions-templates/blob/dev/Functions.Templates/Templates/HttpTrigger-Python/__init__.py
https://github.com/Azure/azure-functions-templates/tree/dev/Functions.Templates/Templates/HttpTrigger-Python
https://github.com/anthonyeden/Azure-Functions-Python-HTTP-Example/blob/master/lib/AzureHTTPHelper.py



"""



"""

"""