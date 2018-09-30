import urllib
import urllib2
import random
import sys

import smtplib

sys.path.append('..')

from credentials import credentials


# def generate_mobile_otp(mobile):
#     # Your authentication key.
#     authkey = ""
#     otp = random.randint(1000, 9999)
#     message = "OTP for registration: %s" % otp
#     # Sender ID,While using route4 sender id should be 6 characters long.
#     sender = "112233"

#     route = "default"

#     # Prepare you post parameters
#     values = {'authkey': authkey,
#               'mobiles': mobile,
#               'message': message,
#               'sender': sender,
#               'route': route
#               }
#     url = ""
#     postdata = urllib.urlencode(values)
#     req = urllib2.Request(url, postdata)
#     response = urllib2.urlopen(req)
#     output = response.read()
#     return otp


def generate_mail_otp(email):

    otp = random.randint(1000, 9999)

    gmail_user = credentials.get('sender')
    gmail_pwd = credentials.get('password')
    FROM = credentials.get('sender')
    SUBJECT = 'OTP'
    TEXT = 'OTP for registration: %s' % otp
    # Prepare actual message
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, email, SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, email, message)
        server.close()
        status = True
        print 'successfully sent the mail'
    except Exception as e:
        status = False
        print "failed to send mail %s" % str(e)
    return {'otp': otp, 'status': status}
