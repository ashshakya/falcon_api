from hashlib import md5
from datetime import datetime

import jwt

from . import verify_token, SECRET_KEY, MONGO_CLIENT
import config
import otp_generate_engine


def register_auth(data):
    """ Method to be used for Registration.
        If email already exists then return a error message otherwise
        creates a new user. All data stored into the mongoDB.
    """
    output = {}
    if data['password'] != data['re-password']:
        return 'Password not matched'
    passwd = str(md5((data['password']).encode('utf-8', 'ignore')).hexdigest())
    name = str(data['name'])
    email = str(data['email'])
    doc = {
        "name": name,
        "email": email,
        "password": passwd,
        "verified": False
    }
    payload = {
        'email': email,
        'token_time': str(datetime.now())
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    res = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if not res:
        doc['otp'] = otp_generate_engine.generate_mail_otp(email)['otp']
        doc['open_timestamp'] = datetime.now()
        MONGO_CLIENT[config.DB_COLL].insert_one(doc)
        output['status'] = 'created'
        output['access_token'] = token
    else:
        output['status'] = "email already exists."
    return output


@verify_token
def otp_verification(data):
    """ Method to verify the OTP.
    """
    output = {}
    otp = data['otp']
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": data['email']})
    if result:
        if result['otp'] == otp:
            doc = {
                "verified": True
            }
            MONGO_CLIENT[config.DB_COLL].update_one({"email": data['email']},
                                                    {'$set': doc})
            output['status'] = 'Verified'
        else:
            output['status'] = 'OTP not matched'
    else:
        output['status'] = 'Record not found'
    return output


def login_auth(email, passwd):
    """ Method to be used to login into the system and
        generated the access_token and maintain session.
    """
    output = {}
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if result:
        if md5(passwd).hexdigest() == result["password"]:
            if result['verified']:
                output['status'] = "success"
                date = datetime.now()
                payload = {
                    'email': email,
                    'token_time': str(date)
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                output['access_token'] = token
            else:
                output['status'] = "not_verified"
        else:
            output['status'] = False
    else:
        output['status'] = "Invalid Credential"
    return output


@verify_token
def file_upload(file):
    """ Method used for adding file path to mongoDB by using
        access_token and checking session of a user for 30 mins.
    """
    output = {}
    file_path = file['filepath']
    email = file['email']
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if result:
        doc = {
            "file_path": file_path
        }
        MONGO_CLIENT[config.DB_COLL].update_one({"email": email},
                                                {'$set': doc})
        output['status'] = "Uploaded"
    else:
        output['status'] = "Not Record Found"
    return output


@verify_token
def upload_detail(data):
    """ Method used to
    """
    output = {}
    email = data['email']
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if result:
        output["file_path"] = result["file_path"]
        output['status'] = True
    else:
        output['status'] = "Not Record Found"
    return output
