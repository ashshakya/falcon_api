#-*- coding:utf-8 -*-
import mysql.connector
import config
# from rrd.utils.logger import logging

db_cfg = {
        "DB_HOST": config.PORTAL_DB_HOST,
        "DB_PORT": config.PORTAL_DB_PORT,
        "DB_USER": config.PORTAL_DB_USER,
        "DB_PASS": config.PORTAL_DB_PASS,
        "DB_NAME": config.PORTAL_DB_NAME,
}


def connect_db(cfg):
    try:
        conn =  mysql.connector.connect(
            host=cfg['DB_HOST'],
            port=cfg['DB_PORT'],
            user=cfg['DB_USER'],
            password=cfg['DB_PASS'],
            database=cfg['DB_NAME'],
            use_unicode=True,
            charset="utf8")

        # if conn:
        #     create_table(conn, sql_create_user_table)
        #     create_table(conn, sql_create_upload_table)
        return conn
    except Exception, e:
        return None



def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Exception as e:
        print(e)


sql_create_upload_table ="""CREATE TABLE IF NOT EXISTS falcon.uploads ( 
                            sno INT NOT NULL AUTO_INCREMENT , 
                            email VARCHAR(100) NOT NULL , 
                            file_path VARCHAR(200) NOT NULL , 
                            datetime DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP , 
                            PRIMARY KEY (sno));"""





sql_create_user_table = """CREATE TABLE IF NOT EXISTS users (
                      sno int(11) NOT NULL AUTO_INCREMENT,
                      name varchar(30) NOT NULL,
                      email varchar(50) NOT NULL,
                      passwd varchar(100) NOT NULL,
                      PRIMARY KEY (sno))
                    ;"""






class DB(object):
    def __init__(self, cfg):
        self.config = cfg
        self.conn = None

    def get_conn(self):
        if self.conn is None:
            self.conn = connect_db(self.config)
        return self.conn


db = DB(db_cfg)
