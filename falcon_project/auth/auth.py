from hashlib import md5
from datetime import datetime

import jwt

from . import verify_token, SECRET_KEY, MONGO_CLIENT
import config
import otp_generate_engine


def get_user_info():
    """ Get all users information."""
    output = {"success": False, "summary": "Get all user data"}
    try:
        res = MONGO_CLIENT[config.DB_COLL].find()
        for user in res:
            doc = {
                'name': user['name'],
                'email': user['email'],
                'verified': user['verified']
            }
            output['user'].append(doc)
        output['success'] = True
    except Exception as e:
        output["summary"] = str(e)
    return output


def register_auth(data):
    """ Method to be used for Registration.
        If email already exists then return a error message otherwise
        creates a new user. All data stored into the mongoDB.
    """
    output = {"success": False, "summary": "User Registration"}
    try:
        if data['password'] != data['re-password']:
            raise Exception("Password not same.")
        passwd = str(md5(
            (data['password']).encode('utf-8', 'ignore')
        ).hexdigest())
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
            output['token'] = token
            output["success"] = True
        else:
            output['summary'] = "Email already exists."
    except Exception as e:
        output["summary"] = str(e)
    return output


def reset_password_otp_request(data):
    """Method to reset password"""
    output = {"success": False, "summary": "OTP Generation on Email"}
    try:
        email = data["email"]
        payload = {
            'email': email,
            'token_time': str(datetime.now())
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        res = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
        if res:
            doc = {
                'otp': otp_generate_engine.generate_mail_otp(email)['otp'],
                'open_timestamp': datetime.now()
            }
            MONGO_CLIENT[config.DB_COLL].update_one(
                {"email": email}, {"$set": doc}
            )
            output['token'] = token
            output["success"] = True
        else:
            output['summary'] = "Email Not Found"
    except Exception as e:
        output["summary"] = str(e)
    return output


@verify_token
def reset_password(data):
    """Method to reset password"""
    output = {"success": False, "summary": "Reset Password"}
    try:
        token = data["token"]
        email = jwt.decode(token, SECRET_KEY, algorithms='HS256')['email']
        payload = {
            'email': email,
            'token_time': str(datetime.now())
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
        res = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
        if res:
            if data['password'] != data['re-password']:
                return 'Password not matched'
            passwd = str(md5(
                (data['password']).encode('utf-8', 'ignore')
            ).hexdigest())
            doc = {
                'password': passwd
            }
            MONGO_CLIENT[config.DB_COLL].update_one(
                {"email": email}, {"$set": doc}
            )
            output['token'] = token
            output["success"] = True
        else:
            output['summary'] = "Email Not Found"
    except Exception as e:
        output["summary"] = str(e)
    return output


@verify_token
def otp_verification(data):
    """ Method to verify the OTP.
    """
    output = {"success": False, "summary": "OTP Verification"}
    try:
        otp = data['otp']
        result = MONGO_CLIENT[config.DB_COLL].find_one(
            {"email": data['email']}
        )
        if result:
            if result['otp'] == otp:
                doc = {
                    "verified": True
                }
                MONGO_CLIENT[config.DB_COLL].update_one(
                    {"email": data['email']}, {'$set': doc}
                )
                payload = {
                    'email': data['email'],
                    'token_time': str(datetime.now())
                }
                token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                output['token'] = token
                output["success"] = True
            else:
                output['summary'] = 'OTP not matched'
        else:
            output['summary'] = 'Record not found'
    except Exception as e:
        output["summary"] = str(e)
    return output


def login_auth(email, passwd):
    """ Method to be used to login into the system and
        generated the token and maintain session.
    """
    output = {"success": False, "summary": "Login"}
    try:
        result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
        if result:
            if md5(passwd).hexdigest() == result["password"]:
                if result['verified']:
                    payload = {
                        'email': email,
                        'token_time': str(datetime.now())
                    }
                    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
                    output['token'] = token
                    output["success"] = True
                else:
                    output['summary'] = "Not Verified"
            else:
                output['summary'] = "Invalid Credential"
        else:
            output['summary'] = "Invalid Credential"
    except Exception as e:
        output["summary"] = str(e)
    return output


@verify_token
def file_upload(file):
    """ Method used for adding file path to mongoDB by using
        token and checking session of a user for 30 mins.
    """
    output = {"summary": False}
    file_path = file['filepath']
    email = file['email']
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if result:
        doc = {
            "file_path": file_path
        }
        MONGO_CLIENT[config.DB_COLL].update_one({"email": email},
                                                {'$set': doc})
        output['summary'] = "Uploaded"
        output["success"] = True
    else:
        output['summary'] = "Not Record Found"
    return output


@verify_token
def upload_detail(data):
    """ Method used to
    """
    output = {"summary": False}
    email = data['email']
    result = MONGO_CLIENT[config.DB_COLL].find_one({"email": email})
    if result:
        output["file_path"] = result["file_path"]
        output['summary'] = True
        output["success"] = True
    else:
        output['summary'] = "Not Record Found"
    return output
