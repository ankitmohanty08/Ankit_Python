from datetime import datetime
import logging
import json
import uuid
import boto3
import bson
import pymongo
from bson import ObjectId, json_util
from botocore.exceptions import ClientError

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    message = event['Records'][0]['body']
    message_dict = json.loads(message)
    logger.info(message_dict)
    client = pymongo.MongoClient(
        "mongodb+srv://singh321:dream321@cluster0.njrzo8e.mongodb.net/?retryWrites=true&w=majority")
    db = client["Aman1"]
    collection = db["user2"]
    collection1=db["user3"]
    mongo_entry = collection.find_one({"TaskId": message_dict['TaskId']})
    mongo_entry = dict(mongo_entry)
    m1_entry=collection1.find_one({"request_id": mongo_entry['request_id']})
   # m_entry =collection.find_one({"TaskId":  mongo_entry['parentTaskId']})
    print("This is mongo Entry", mongo_entry)
    z1 = uuid.uuid4()
    z1 = str(z1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg_body = {
        "Name":"Lambda4",
        "request_id": mongo_entry['request_id'],
        "parentTaskId": mongo_entry['TaskId'],
        "TaskId": z1,
        "request_time": current_time,
        "counter": 1,
        "status": 1,
    }
    collection.insert_one(msg_body)
    result = collection1.update_one({"request_id": mongo_entry['request_id']},
                                   {"$set": {"value1": m1_entry['a'] * m1_entry['b']}},
                                   upsert=False)

    #result = collection.update_one({ "TaskId": z1},
                                  # {"$set": {"value1": m1_entry['a']*m1_entry['b']}},
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
                              {"$set": {"status" :"0"}},
                              upsert=False)

    collection.update_one({"TaskId": message_dict['TaskId']},
                          {"$set": {"counter": test1["counter"] - 1}},
                          upsert=False)

