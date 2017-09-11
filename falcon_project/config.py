#-*-coding:utf8-*-
# app config
import os

# portal database
# TODO: read from api instead of db
PORTAL_DB_HOST = os.environ.get("PORTAL_DB_HOST","127.0.0.1")
PORTAL_DB_PORT = int(os.environ.get("PORTAL_DB_PORT",3306))
PORTAL_DB_USER = os.environ.get("PORTAL_DB_USER","root")
PORTAL_DB_PASS = os.environ.get("PORTAL_DB_PASS","")
PORTAL_DB_NAME = os.environ.get("PORTAL_DB_NAME","falcon")