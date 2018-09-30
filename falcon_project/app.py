"""
This code creates your WSGI application and aliases it as api.
This module perform basic api operations like registration,
login, upload a file path and details.
"""
from __future__ import unicode_literals
import json

import falcon

from auth import auth


class RegisterClass:
    """ Registration Api"""
    def on_get(self, req, resp):
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.register_auth(data)
            if output.get("success", False):
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
            else:
                resp.status = falcon.HTTP_202
                resp.body = json.dumps(output)
        except Exception as k:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'output': str(k)})


class OptVerificationClass:
    """ OTP Verification API"""
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.otp_verification(data)
            if output.get("success", False):
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
            else:
                resp.status = falcon.HTTP_202
                resp.body = json.dumps(output)
        except Exception as k:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'output': str(k)})


class LoginClass:
    """ Login api. """
    def on_get(self, req, resp):
        # resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            email = data['email']
            passwd = data['password']
            output = auth.login_auth(email, passwd)
            if output.get("success", False):
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
            else:
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
        except Exception as k:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'output': str(k)})


class UploadClass:
    """ Upload Api """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.file_upload(data)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
        except Exception as k:
            resp.body = json.dumps({'output': str(k)})


class DetailClass:
    """ Detail Api """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.upload_detail(data)
            resp.status = falcon.HTTP_200
            resp.body = json.dumps(output)
        except Exception as k:
            resp.body = json.dumps({'output': str(k)})


class ResetPasswordOtpRequestClass:
    """ Password Reset otp request  """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.reset_password_otp_request(data)
            if output.get("success", False):
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
            else:
                resp.status = falcon.HTTP_202
                resp.body = json.dumps(output)
        except Exception as k:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'output': str(k)})


class ResetPasswordClass:
    """ Reset Password """
    def on_get(self, req, resp):
        resp.status = falcon.HTTP_405
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        try:
            data = json.loads(req.stream.read())
            output = auth.reset_password(data)
            if output.get("success", False):
                resp.status = falcon.HTTP_200
                resp.body = json.dumps(output)
            else:
                resp.status = falcon.HTTP_401
                resp.body = json.dumps(output)
        except Exception as k:
            resp.status = falcon.HTTP_400
            resp.body = json.dumps({'output': str(k)})


# class GetUserClass:
#     """ Get all user details."""
#     def on_get(self, req, resp):
#         try:
#             output = auth.get_user_info()
#             if output.get("success", False):
#                 resp.status = falcon.HTTP_200
#                 resp.body = json.dumps(output)
#             else:
#                 resp.status = falcon.HTTP_202
#                 resp.body = json.dumps(output)
#         except Exception as k:
#             resp.status = falcon.HTTP_400
#             resp.body = json.dumps({'output': str(k)})
