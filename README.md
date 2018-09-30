# Falcon Basic Accounts Authentication API's

A Falcon app in python that has following Api's:

1) Register/Create Account
2) Verify the account with otp recieved in email that provided.
3) Users will be able to login into their account using email & password.
4) Users will be able to make a entry in db and view records of own account.

Application also have funcationality to reset password.


-----------------------------------------------------------------------------------------------------------------------------------

Create your virtual environment and install all dependent libraries by running following command:

    pip install -r requirement.txt

To Register : `/api/v1/Register/`
Method : POST
Param : `{
        "name" : ,
        "email": ,
        "password" : ,
        "re-password" :
    }`

To Verify with OTP: `/api/v1/Verify/`
Method : POST
Param : `{
    "name" : ,
    "email": ,
    "access_token": ,
    "otp": ,
}`

To Login : `/api/v1/Login/`
Method : POST
Param : `{
    "email" : ,
    "password" :
}`

To Upload : `/api/v1/Upload/`
Method : POST
Param : `{
    "filepath": ,
    "email": ,
    "access_token"
}`

To get Details : `/api/v1/Detail/`
Method : POST
Param : `{
    "email": ,
    "access_token" :
}`

    git clone git@github.com:ashshakya/falcon_api.git
    cd falcon_api/falcon_project
    pip install -r ../requirement.txt
    python runserver.py


