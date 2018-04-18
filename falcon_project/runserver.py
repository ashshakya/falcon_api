import falcon
from werkzeug.serving import run_simple

from app import *

api = falcon.API()
api.add_route('/api/v1/Login/', LoginClass())
api.add_route('/api/v1/Register/', RegisterClass())
api.add_route('/api/v1/Upload/', UploadClass())
api.add_route('/api/v1/Detail/', DetailClass())
api.add_route('/api/v1/verify/', OptVerificationClass())

if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, api, use_reloader=True)
