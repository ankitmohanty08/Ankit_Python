from datetime import datetime
import uuid

import boto3
import pymongo
import json
from botocore.exceptions import ClientError
import bson
from bson import ObjectId

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event,context):
    message = event['Records'][0]['body']
    logger.info(message)
    message_dict = json.loads(message)
    logger.info(message_dict)
    client = pymongo.MongoClient("mongodb+srv://singh321:dream321@cluster0.njrzo8e.mongodb.net/?retryWrites=true&w=majority")
    db = client["Aman1"]
    collection = db["user2"]
    collection1 = db["user3"]
    mongo_entry = collection.find_one({"TaskId": message_dict['TaskId']})
    mongo_entry=dict(mongo_entry)
    m_entry = collection1.find_one({ "request_id": mongo_entry['request_id']})
    logger.info(mongo_entry)
    z1 = uuid.uuid4()
    z1 = str(z1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg_body = {
        "Name": "Lambda5",
        "request_id": mongo_entry['request_id'],
        "parentTaskId": mongo_entry['TaskId'],
        "TaskId": z1,
        "request_time": current_time,
        "counter": 1,
        "status": 1,
    }
    collection.insert_one(msg_body)
    try:
        value= (m_entry['sum'] * m_entry['diff'])/ m_entry['c']
    except ZeroDivisionError as e:
        value="Not defined"
    result = collection1.update_one({ "request_id": mongo_entry['request_id']},
                                   {"$set": {"value2": value}},
                                   upsert=False)

    #result = collection.update_one({"TaskId": z1},
                                 #  {"$set": {"value2": value}},
                                  # upsert=False)
    logger.info(result)
    m1 = {
        "TaskId": z1
    }
    test1 = collection.find_one({"TaskId": message_dict['TaskId']})
    test1 = dict(test1)
    if test1["counter"] == 1:
        sqs_client = boto3.client('sqs')
        sqs_queue_url = "https://sqs.ap-south-1.amazonaws.com/611334599981/dev-lambda3-poc"
        try:
            msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                          MessageBody=json.dumps(m1))
            logger.info(msg)
        except ClientError as e:
            logger.info(e)
            return None
        collection.update_one({"TaskId": message_dict['TaskId']},
                              {"$set": {"status": "0"}},
                              upsert=False)
    collection.update_one({"TaskId": message_dict['TaskId']},
                          {"$set": {"counter": test1["counter"] - 1}},
                          upsert=False)
