"""
This code creates your WSGI application and aliases it as api.
This module perform basic api operations like registration, login, upload a file path and details.
"""
import json

import falcon

from auth import auth


class LoginClass:
    """ Login api. """
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            username = d['username']
            passwd = d['password']
            output = auth.login_auth(username, passwd)
            if output['status'] == 'success':
                resp.body = json.dumps(output)
            else:
                resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class RegisterClass:
    """ Registration Api"""
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.register_auth(d)
            if output == 'created':
                resp.body = json.dumps(output)
            else:
                resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class UploadClass:
    """ Upload Api """
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.file_upload(d)
            if output['status'] == 'Uploaded':
                resp.body = json.dumps(output)
            else:
                resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


class DetailClass:
    """ Detail Api """
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        try:
            d = json.loads(req.stream.read())
            output = auth.upload_detail(d)
            if output['status']:
                resp.body = json.dumps(output)
            else:
                resp.body = json.dumps(output)
        except KeyError as k:
            resp.body = json.dumps({'output': k})


api = falcon.API()


api.add_route('/falcon/api/Login/', LoginClass())
api.add_route('/falcon/api/Register/', RegisterClass())
api.add_route('/falcon/api/Upload/', UploadClass())
api.add_route('/falcon/api/Detail/', DetailClass())
