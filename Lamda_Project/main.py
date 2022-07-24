import logging
import json
import pymongo
import boto3
import uuid
from datetime import datetime
from botocore.exceptions import ClientError
from bson import json_util
logger = logging.getLogger()
logger.setLevel(logging.INFO)


def send_sqs_message(sqs_queue_url, msg_body):
    client = pymongo.MongoClient(
        "mongodb+srv://singh321:dream321@cluster0.njrzo8e.mongodb.net/?retryWrites=true&w=majority")
    db = client["Aman1"]
    collection = db["user2"]
    collection1=db["user3"]
    z=uuid.uuid4()
    z=str(z)
    z1 = uuid.uuid4()
    z1 = str(z1)
    now=datetime.now()
    current_time=now.strftime("%H:%M:%S")
    msg_body = {
        "request_id":z,
        "TaskId":z1,
        "request_time":current_time,
        "counter":2,
        "status":1,
    }
    msg1={
        "request_id": z,
        "a": 8,
        "b": 2,
        "c": 4,
    }
    collection1.insert_one(msg1)
    msg_body=dict(msg_body)
    m1={
        "request_id":z
    }
    print(z)
    print(json.dumps(m1))
    print(json_util.dumps(m1))
    x = collection.insert_one(msg_body)
    # Send the SQS message
    sqs_client = boto3.client('sqs')
    sqs_queue_url = "https://sqs.ap-south-1.amazonaws.com/611334599981/dev-lambda1-poc"
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=json.dumps(m1))
        print(msg)
    except ClientError as e:
        return None

    sqs_queue_url = "https://sqs.ap-south-1.amazonaws.com/611334599981/dev-lambda2-poc"
    try:
        msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
                                      MessageBody=json.dumps(m1))
        print(msg)
    except ClientError as e:
        return None


    # msg_body = {
    #     "c": 3
    # }
    # sqs_queue_url = "https://sqs.ap-south-1.amazonaws.com/611334599981/dev-lambda3-poc"
    # try:
    #     msg = sqs_client.send_message(QueueUrl=sqs_queue_url,
    #                                   MessageBody=json.dumps(msg_body))
    # except ClientError as e:
    #     return None


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    send_sqs_message("", "")
