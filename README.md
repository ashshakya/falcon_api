# falcon_api

Create your virtual environment and run following command:
    pip install -r requirement.txt

In this, Api uses Mysql as database. So, user must have mysql as backend to store the data. To store data api require python mysql connector that can be install by using following command:
    sudo apt-get install update
    sudo apt-get install python-mysqldb

Change mysql credentials in config.py.


user can import falcon_api.postman_collection.json into your postman app and directly access the api.

            OR
Manually enter the following paramerter and header content to use this Api .

To Register : {host_ip}:{host:port}/falcon/api/Register/
Method : POST
header : {
            Content-Type:application/json,
            action:register,
            auth_key:qwertyuiop,
        }
Param :
    {
        "name" : ,
        "email": ,
        "password" : ,
        "re-password" :
    }


To Login : {host_ip}:{host:port}/falcon/api/Login/
Method : POST
header : {
            Content-Type:application/json,
            action:register,
            auth_key:qwertyuiop,
        }

Param : {
	"username" : ,
	"password" :
}

To Upload : {host_ip}:{host:port}/falcon/api/Upload/
Method : PUT
header :{
            Content-Type:application/json,
            action:upload,
            auth_key:qwertyuiop,
        }

Param : {
	"filepath": ,
	"email":
}

To get Details : {host_ip}:{host:port}/falcon/api/Detail/
Method : POST
header : {
            Content-Type:application/json,
            action:detail,
            auth_key:qwertyuiop,
        }
Param :{
	"email": ,
	"session_id" :
}