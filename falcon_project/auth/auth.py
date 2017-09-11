from falcon_project import store
from hashlib import md5


def register_auth(data):
    output = ''
    conn = store.connect_db(store.db_cfg)
    cur = conn.cursor(buffered=True)
    print data
    if data['password'] != data['re-password']:
        return 'Password not matched'
    passwd = str(md5((data['password']).encode('utf-8', 'ignore')).hexdigest())
    print '909090   '
    name = str(data['name'])
    email = str(data['email'])
    print name, email, passwd
    try:
        q = "INSERT INTO users (`name`, `email`, `passwd`) VALUES ('%s', '%s', '%s')" %(name, email, passwd)
        print q
        cur.execute(q)
        conn.commit()
        output['status'] = 'created'
    except Exception as e:
        print e
        output['status'] = e
    finally:
        cur.close()
        return output


def login_auth(user, passwd):
    output = {}
    conn = store.connect_db(store.db_cfg)
    cur = conn.cursor(buffered=True)
    # check.execute('select id')
    email = ''
    cur.execute("SELECT email FROM users WHERE email = %s;", [user]) # CHECKS IF USERNAME EXSIST
    for row in cur:
        email = row[0]
    try:
        if email:
            cur.execute("SELECT passwd FROM users WHERE email = %s;", [user]) # FETCH THE HASHED PASSWORD
            for row in cur:
                if md5(passwd).hexdigest() == row[0]:
                    output['status'] = 'Loged IN'
                else:
                    output['status'] = 'Paswword Invalid'
        else:
            output['status'] = "Invalid Credential"
    except Exception as e:
        output['status'] = e
    cur.close()
    return output


def file_upload(file):
    output = {}
    conn = store.connect_db(store.db_cfg)
    cur = conn.cursor(buffered=True)
    file_path = file['filepath']
    email = file['email']
    try:
        q = "INSERT INTO `uploads`(`email`, `file_path`) VALUES ('{0}', '{1}')".format(email, file_path)
        print q
        cur.execute(q)
        conn.commit()
        output['status'] = 'Uploaded'
    except Exception as e:
        output['status'] = str(e)
    finally:
        return output


def upload_detail(data):
    output = {}
    conn = store.connect_db(store.db_cfg)
    cur = conn.cursor(buffered=True)
    email = data['email']
    try:
        query = "SELECT file_path, datetime FROM uploads WHERE email = '{}'".format(email)
        cur.execute(query)
        for row in cur:
            output[str(row[1])] = row[0]
            output['status'] = 'Done'
    except Exception as e:
        output['status'] = str(e)
    finally:
        return output