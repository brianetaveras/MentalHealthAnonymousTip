from twilio.rest import Client
from collections import deque  


class SMSHandler:
    def __init__(self, account_sid, auth_token):
        self.account_sid = account_sid
        self.auth_token = auth_token
        self.twilio_client = None
        self.queue = deque()
        self.initializeTwilioClient()
        self.initializeMessageQueue()

    def initializeTwilioClient(self):
        self.twilio_client = Client(self.account_sid, self.auth_token)

    def initializeMessageQueue(self):
        while self.queue:
            current_message = self.queue.pop()
            self.sendMessage(current_message)
            console.log('sent a message')

    def sendMessage(self, message):
        message = self.twilio_client.messages.create(
                    to= message["number"], 
                    from_= "+19728454955",
                    body="Hello from Python!")
                        

    def addMessageToQueue(self, message):
        self.queue.append(message)
        print("Message added to queue")


