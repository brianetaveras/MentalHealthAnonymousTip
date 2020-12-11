import os
import re
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

        if not isValidNumber(request_body):
            return HttpResponse("Must provide a valid number", status=400)
        
        message_body = getMessageBody(request_body["lang"])
        
        messageHandler.sendMessage({
            "number": request_body["number"],
            "body": message_body
        })
        return HttpResponse("Message successful")
    except Exception as err:
        print(err)
        return HttpResponse("There was an issue while sending the message. Please try again later", status=500)
        

def getMessageBody(language="EN"):
    message = TextMessage.objects.filter(language_code=language).first()

    if not message:
        message = TextMessage.objects.filter(language_code="EN").first()

    return message.message_body

def isValidNumber(message_information):
    if (message_information["number"]):
        phone_validator = re.compile("^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$")
        if(phone_validator.match(message_information["number"])):
            return True
    return False
    