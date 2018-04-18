import urllib
import urllib2
import random

import smtplib

def generate_mobile_otp(mobile):
    # Your authentication key.
    authkey = "209774A4F0FnL95ad05494"
    otp = random.randint(1000, 9999)
    message = "OTP for registration: %s" % otp
    # Sender ID,While using route4 sender id should be 6 characters long.
    sender = "112233"

    route = "default"

    # Prepare you post parameters
    values = {'authkey': authkey,
              'mobiles': mobile,
              'message': message,
              'sender': sender,
              'route': route
              }
    url = "https://control.msg91.com/api/sendhttp.php"
    postdata = urllib.urlencode(values)
    req = urllib2.Request(url, postdata)
    response = urllib2.urlopen(req)
    output = response.read()
    return otp


def generate_mail_otp(email):

    otp = random.randint(1000, 9999)

    gmail_user = "asashwanishakya@gmail.com"
    gmail_pwd = "@sh477108sonu"
    FROM = "asashwanishakya@gmail.com"
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
