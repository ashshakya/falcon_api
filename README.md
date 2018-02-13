# Falcon Basic API's

A Falcon app in python that has following Api's:

1) Register/Create Account
2) Users should be able to login into their account using user & pass
3) Users should be able to upload files and to their account
      --  This should be an API defining only the name of the file that user wants to upload.
           save the filename in the database.( Actual upload of file is not required )


4) Each user should be able to list the names of files uploaded by them and for each file show the time of upload.

-----------------------------------------------------------------------------------------------------------------------------------

Create your virtual environment and install all dependent libraries by running following command:

    pip install -r requirement.txt

To Register : {host_ip}:{host:port}/falcon/api/Register/
Method : POST
Param :
    {
        "name" : ,
        "email": ,
        "password" : ,
        "re-password" :
    }


To Login : {host_ip}:{port}/falcon/api/Login/
Method : POST
Param : {
	"username" : ,
	"password" :
}

To Upload : {host_ip}:{host:port}/falcon/api/Upload/
Method : POST
Param : {
	"filepath": ,
	"email": ,
    "access_token"
}

To get Details : {host_ip}:{host:port}/falcon/api/Detail/
Method : POST
Param :{
	"email": ,
	"access_token" :
}

	git clone git@github.com:ashshakya/falcon_api.git
	cd falcon_api
	pip install -r requirement.txt
	gunicorn --reload falcon_api.app


