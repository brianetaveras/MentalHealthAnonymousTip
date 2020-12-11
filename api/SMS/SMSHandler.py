from twilio.rest import Client
from collections import deque  


class SMSHandler:
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_client = None
        self.initializeTwilioClient()

    def initializeTwilioClient(self):
        self.twilio_client = Client(self.account_sid, self.auth_token)


    def sendMessage(self, message):
        message = self.twilio_client.messages.create(
                    to= message["number"], 
                    from_= "+19728454955",
                    body= message["body"])
                        


