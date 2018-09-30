from datetime import datetime

from pymongo import MongoClient
import jwt

import config

SECRET_KEY = '1234567890qwertyuiop'
MONGO_CLIENT = MongoClient(config.DB_HOST)[config.DB_NAME]


def verify_token(func):

    def decorator(*args, **kwargs):
        token = args[0]['token']
        try:
            decode_data = jwt.decode(token, SECRET_KEY, algorithms='HS256')
            decode_token = decode_data.get("token_time", None)
            decode_token_time = datetime.strptime(decode_token,
                                                  "%Y-%m-%d %H:%M:%S.%f")
            if decode_token_time is not None:
                if (datetime.now() - decode_token_time).seconds > 3600:
                    return "Session Expire"
            else:
                return "Token not present."
        except jwt.DecodeError as err:
            return "Access Token Failed due to %s" % err
        return func(*args, **kwargs)

    return decorator
