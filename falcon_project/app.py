"""
This code creates your WSGI application and aliases it as api.
This module perform basic api operations like registration, login, upload a file path and details.
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
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.register_auth(d)
            resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class OptVerificationClass:
    """ Registration Api"""
    def on_get(self, req, resp):
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            data = json.loads(req.stream.read())
            output = auth.otp_verification(data)
            resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class LoginClass(object):
    """ Login api. """
    def on_get(self, req, resp):
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            email = d['email']
            passwd = d['password']
            output = auth.login_auth(email, passwd)
            output['email'] = email
            resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class UploadClass:
    """ Upload Api """
    def on_get(self, req, resp):
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.file_upload(d)
            resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class DetailClass:
    """ Detail Api """
    def on_get(self, req, resp):
        resp.body = json.dumps({'output':
                               "Hey, I think you are on wrong page."})

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.upload_detail(d)
            resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})
