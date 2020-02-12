"""
Demo :  send events to Azure EventHub (sync), then these events will 
        be processed in Azure Stream Analytics and written to Blob.
        We'll be using SlidingWindow().

Requirements :
    - provison Azure Stream Analytics
    - setup input -> EvenetHub
    - setup output -> Blob
    - set up the Azure Stream Analytics Query :
        SELECT
            input01.job, count(*)
        INTO
            [output01]
        FROM
            [input01] TIMESTAMP BY EventTime
        GROUP BY input01.job, SlidingWindow(second, 8)

Azure EventHub, Azure Stream Analytics, Azure Storage - Blob
"""

# https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub/samples/sync_samples [the built number]
# https://github.com/YijunXieMS/azure-sdk-for-python/blob/master/sdk/eventhub/azure-eventhub/samples/sync_samples/send_stream.py
# https://github.com/YijunXieMS/azure-sdk-for-python/blob/master/sdk/eventhub/azure-eventhub/samples/sync_samples/send.py
# https://github.com/Azure/azure-sdk-for-python/tree/master/sdk/eventhub/azure-eventhub/samples

import json
import time
import logging
import uuid
import sys
import datetime
from azure.eventhub import EventHubProducerClient
from azure.eventhub import EventData

# log to stout
# logger = logging.getLogger('Azure_EventHub')
# handler = logging.StreamHandler(sys.stdout)
# logger.setLevel(logging.INFO)
# logger.addHandler(handler)

# log to log file
logger = logging.getLogger('Azure_EventHub')
handler = logging.FileHandler('eventhub.log')
logger.setLevel(logging.INFO)
logger.addHandler(handler)


SAS_KEY = ""
EVENTHUB_NAME = "hub01"

producer = EventHubProducerClient.from_connection_string(conn_str = SAS_KEY, eventhub_name=EVENTHUB_NAME)
event_data_batch = producer.create_batch()


with producer:
    for e in range(100000) :
        if e%3 == 0:
            x = { "id":str(uuid.uuid4()), "job": "student", "age": e, "EventTime": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'}
            event_data  = EventData(json.dumps(x))
            #time.sleep(0.5)
        else :
            x = {  "id":str(uuid.uuid4()),"job": "manager", "age": e+1, "EventTime": datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z' }
            event_data  = EventData(json.dumps(x))
        logger.info("new event : {}".format(e))
        try :
            event_data_batch.add(event_data)
        except ValueError as error:
            # writing messages to EventHub
            logger.info("Exception {}".format(error))
            logger.info("trying to write events batch to Azure : {}".format(len(event_data_batch)))
            producer.send_batch(event_data_batch)

            # create new batch to pick up where we stopped
            logger.info("create a new batch instance to pick up where we stopped")
            event_data_batch = producer.create_batch()
            event_data_batch.add(event_data)
    
    if len(event_data_batch) > 0:
        # writing messages to EventHub if we don't hit the Exception
        logger.info("No Exceptopn -> trying to write events batch to Azure : {}".format(len(event_data_batch)))
        producer.send_batch(event_data_batch)
