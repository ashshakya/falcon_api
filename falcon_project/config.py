#-*-coding:utf8-*-
# app config
import os

# portal database
# TODO: read from api instead of db
DB_HOST = os.environ.get("DB_HOST", None)
DB_PORT = int(os.environ.get("DB_PORT", None))
DB_NAME = os.environ.get("DB_NAME", None)
DB_COLL = os.environ.get("DB_COLLECTION", None)
