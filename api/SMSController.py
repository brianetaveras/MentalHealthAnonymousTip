import os
import json
from .models import TextMessage
from django.shortcuts import render
from .SMS.SMSHandler import SMSHandler
from django.http.response import HttpResponse
# Create your views here.


def SMS(request):
    # TODO error handling/input validation
    try:
        messageHandler = SMSHandler(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
        
        request_body = json.loads(request.body)
        
        message_body = getMessageBody(request_body["lang"])
        
        # messageHandler.sendMessage({
        #     "number": request_body["number"],
        #     "body": message_body
        # })
        # message_body.plop()
        return HttpResponse("Message successful")
    except Exception as err:
        print(err)
        return HttpResponse("There was an issue while sending the message. Please try again later", status=500)
        

def getMessageBody(language):
    message = TextMessage.objects.filter(language_code=language).first()

    if not message:
        message = TextMessage.objects.filter(language_code="EN").first()

    return message.message_body