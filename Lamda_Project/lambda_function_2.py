from datetime import datetime
import smtplib
import uuid

import pymongo
import json
import bson
from bson import ObjectId

import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)
def send_email(value):
    gmail_user = 'aman.k@karza.in'
    gmail_app_password = "Dream@#123"
    sent_from = gmail_user
    sent_to = ['izrail.m@karza.in']
    sent_subject = "Calculation value"
    sent_body = "Result of the calculation is " + str(value)

    email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(sent_to), sent_subject, sent_body)

    try:
        logger.info("Inside try")
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_app_password)
        server.sendmail(sent_from, sent_to, email_text.encode("utf-8"))
        server.close()
        print(email_text)
        logger.info('Email sent!')
    except Exception as exception:
        logger.error(exception)


def lambda_handler(event, context, ):
    message = event['Records'][0]['body']
    logger.info(message)
    message_dict = json.loads(message)
    logger.info(message_dict)
    client = pymongo.MongoClient("mongodb+srv://singh321:dream321@cluster0.njrzo8e.mongodb.net/?retryWrites=true&w"
                                 "=majority")
    db = client["Aman1"]
    collection = db["user2"]
    collection1 = db["user3"]
    mongo_entry = collection.find_one({"TaskId":message_dict["TaskId"]})
    m_entry=collection1.find_one({ "request_id": mongo_entry['request_id']})
    logger.info(mongo_entry)
    z1 = uuid.uuid4()
    z1 = str(z1)
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    msg_body = {
        "Name": "Lambda3",
        "request_id": mongo_entry['request_id'],
        "parentTaskId": mongo_entry['TaskId'],
        "TaskId": z1,
        "request_time": current_time,
    }
    x = collection.insert_one(msg_body)
    value = m_entry['value1'] + m_entry['value2']
    result = collection1.update_one({"request_id": mongo_entry['request_id']},
                                   {"$set": {"Result": value}},
                                   upsert=False)

    result = collection.update_one({"TaskId":mongo_entry['TaskId']},
                                  {"$set": {"status":0}},
                                  upsert=False)
    collection.update_one({"TaskId":mongo_entry['TaskId']},
                          {"$set": {"counter": mongo_entry["counter"]-1}},
                          upsert=False)
    logger.info(result)
    value = m_entry['value1'] + m_entry['value2']
    logger.info(value)
    #send_email(value)
