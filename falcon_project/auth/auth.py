from hashlib import md5
import base64
from datetime import datetime

from pymongo import MongoClient
import config


def register_auth(data):
    output = {}
    db = MongoClient(config.DB_HOST)[config.DB_NAME]
    if data['password'] != data['re-password']:
        return 'Password not matched'
    passwd = str(md5((data['password']).encode('utf-8', 'ignore')).hexdigest())
    name = str(data['name'])
    email = str(data['email'])
    doc = {
        "name": name,
        "email": email,
        "password": passwd
    }
    res = db[config.DB_COLLECTION].find_one({"email": email})
    if not res:
        db[config.DB_COLLECTION].insert_one(doc)
        output['status'] = 'created'
    else:
        output['status'] = "email already exists."
    return output


def login_auth(email, passwd):
    output = {}
    db = MongoClient(config.DB_HOST)[config.DB_NAME]
    result = db[config.DB_COLLECTION].find_one({"email": email})
    if result:
        if md5(passwd).hexdigest() == result["password"]:
            output['status'] = "success"
            date = datetime.now()
            token = base64.b64encode(email) + base64.b64encode(str(date))
            doc = {
                "date": date,
                "token": token
            }
            db[config.DB_COLLECTION].update_one({"email": email},
                                                {'$set': doc})
            output['access_token'] = token
        else:
            output['status'] = False
    else:
        output['status'] = "Invalid Credential"
    return output


def file_upload(file):
    output = {}
    db = MongoClient(config.DB_HOST)[config.DB_NAME]
    file_path = file['filepath']
    email = file['email']
    result = db[config.DB_COLLECTION].find_one({"email": email})
    if result:
        if result["token"] == file['access_token']:
            now = datetime.now()
            if (now - result["date"]).seconds < 300:
                doc = {
                    "file_path": file_path
                }
                db[config.DB_COLLECTION].update_one({"email": email},
                                                    {'$set': doc})
                output['status'] = "Uploaded"
            else:
                output['status'] = "session failed"
        else:
            output['status'] = "Not authorized."
    else:
        output['status'] = "Not Record Found"
    return output


def upload_detail(data):
    output = {}
    db = MongoClient(config.DB_HOST)[config.DB_NAME]
    email = data['email']
    result = db[config.DB_COLLECTION].find_one({"email": email})
    if result:
        if result["token"] == data['access_token']:
            now = datetime.now()
            if (now - result["date"]).seconds < 300:
                detail = db[config.DB_COLLECTION].find_one({"email": email})
                output["file_path"] = detail["file_path"]
                output['status'] = True
            else:
                output['status'] = "session failed"
        else:
            output['status'] = "Not authorized."
    else:
        output['status'] = "Not Record Found"
    return output
