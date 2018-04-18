import falcon

from app import *

api = falcon.API()
api.add_route('/api/v1/Login/', LoginClass())
api.add_route('/api/v1/Register/', RegisterClass())
api.add_route('/api/v1/Upload/', UploadClass())
api.add_route('/api/v1/Detail/', DetailClass())
api.add_route('/api/v1/verify/', OptVerificationClass())
