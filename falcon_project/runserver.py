import falcon

from __init__ import *
from app import *

api = falcon.API()
api.add_route('/api/v1/Login/', LoginClass())
api.add_route('/api/v1/Register/', RegisterClass())
api.add_route('/api/v1/Upload/', UploadClass())
api.add_route('/api/v1/Detail/', DetailClass())
api.add_route('/api/v1/Verify/', OptVerificationClass())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('0.0.0.0', 8000, api)
    httpd.serve_forever()
