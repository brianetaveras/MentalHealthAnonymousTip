from django.shortcuts import render
from .SMS.SMSHandler import SMSHandler
import json
from django.http.response import HttpResponse
import os
# Create your views here.

class SMSController:

    def SMS(request):

        try:
            messageHandler = SMSHandler(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
            message = json.loads(request.body)
            messageHandler.sendMessage(message)

            return HttpResponse("ok")
        except Error:
            print("Something horrible happened", Error)
            return HttpResponse("not ok")
    
    def getMessageBody(self, language):
        pass