import os
import json
from .models import TextMessage
from django.shortcuts import render
from .SMS.SMSHandler import SMSHandler
from django.http.response import HttpResponse
# Create your views here.


def SMS(request):
    # TODO error handling/input validation
    messageHandler = SMSHandler(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])
    
    request_body = json.loads(request.body)
    
    message_body = getMessageBody(request_body["lang"])
    
    messageHandler.sendMessage({
        "number": request_body["number"],
        "body": message_body
    })

    return HttpResponse("Message successful")


def getMessageBody(language):
    message = TextMessage.objects.filter(language_code=language).first()

    if not message:
        message = TextMessage.objects.filter(language_code="EN").first()

    return message.message_body