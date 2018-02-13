#-*-coding:utf8-*-
# app config
import os

# portal database
# TODO: read from api instead of db
DB_HOST = os.environ.get("DB_HOST", "127.0.0.1")
DB_PORT = int(os.environ.get("DB_PORT", 27017))
DB_NAME = os.environ.get("DB_NAME", "falcon")
DB_COLLECTION = os.environ.get("DB_COLLECTION", "upload")
