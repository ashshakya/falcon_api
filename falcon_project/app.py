"""
This code creates your WSGI application and aliases it as api.
"""


import falcon, json
from auth import auth


class LoginClass:

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        h = req.headers
        try:
            if h['AUTH-KEY'] == 'qwertyuiop':
                if h['ACTION'] == 'login':
                    d = json.loads(req.stream.read())
                    username = d['username']
                    passwd = d['password']
                    output = auth.login_auth(username, passwd)
                    if output['status'] == 'success':
                        resp.body = json.dumps(output)
                    else:
                        resp.body = json.dumps(output)
            else:
                resp.body = json.dumps({'output': 'auth key not matched'})
        except KeyError:
            resp.body = json.dumps({'output': 'Auth Key not Found'})


class RegisterClass:

    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200

        h = req.headers
        try:
            print '==='
            if h['AUTH-KEY'] == 'qwertyuiop':
                print '=111=='
                if h['ACTION'] == 'register':
                    print '===222'
                    d = json.loads(req.stream.read())
                    output = auth.register_auth(d)
                    print output
                    if output == 'created':
                        resp.body = json.dumps(output)
                    else:
                        resp.body = json.dumps(output)
            else:
                resp.body = json.dumps({'output': 'auth key not matched'})
        except KeyError:
            resp.body = json.dumps({'output': 'Auth Key not Found'})


class UploadClass:

    def on_put(self, req, resp):
        resp.status = falcon.HTTP_200

        h = req.headers
        try:
            if h['AUTH-KEY'] == 'qwertyuiop':
                if h['ACTION'] =='upload':
                    d = json.loads(req.stream.read())
                    output = auth.file_upload(d)
                    if output['status'] == 'Uploaded':
                        resp.body = json.dumps(output)
                    else:
                        resp.body = json.dumps(output)
            else:
                resp.body = json.dumps({'output': 'auth key not matched'})
        except KeyError as k:
            resp.body = json.dumps({'output': 'Auth Key not Found :{}'.format(k)})


class DetailClass:
    def on_post(self, req, resp):
        resp.status = falcon.HTTP_200
        h = req.headers
        try:
            if h['AUTH-KEY'] == 'qwertyuiop':
                if h['ACTION'] =='detail':
                    d = json.loads(req.stream.read())
                    output = auth.upload_detail(d)
                    if output['status'] == 'Uploaded':
                        resp.body = json.dumps(output)
                    else:
                        resp.body = json.dumps(output)
            else:
                resp.body = json.dumps({'output': 'auth key not matched'})
        except KeyError as k:
            resp.body = json.dumps({'output': 'Auth Key not Found :{} \n {}'.format(k, output)})

api = application = falcon.API()


api.add_route('/falcon/api/Login/', LoginClass())
api.add_route('/falcon/api/Register/', RegisterClass())
api.add_route('/falcon/api/Upload/', UploadClass())
api.add_route('/falcon/api/Detail/', DetailClass())
