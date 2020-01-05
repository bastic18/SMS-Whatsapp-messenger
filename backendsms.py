from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = sid  # sid should be place here 
auth_token =  auth #  auth token should be place here 
client = Client(account_sid, auth_token)
numsms= '1##########'   # number from twilio is given here for regaulr sms 
numwts='whatsapp:+1##########'   # number from twilio given as trial is used here for whatsapp message 

def sms(self,tosms,msg):
    message = client.messages.create(
         body=msg,
         from_=numsms,
         to=tosms
     )

    print(message.sid)


def whatsapp(self,towts,msg):
    message = client.messages.create(
         body=msg,
         from_=numwts,
         to='whatsapp:'+ towts
     )

    print(message.sid)