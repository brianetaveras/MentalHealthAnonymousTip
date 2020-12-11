import os
import re
import json
import hashlib
from .models import TextMessage, HashedNumber
from django.shortcuts import render
from .SMS.SMSHandler import SMSHandler
from django.http.response import HttpResponse
# Create your views here.


def SMS(request):
    # TODO error handling/input validation
    try:
        
        request_body = json.loads(request.body)

        if not isValidNumber(request_body):
            return HttpResponse("Must provide a valid number", status=400)

        hashed_number = cleanAndHashNumber(request_body["number"])
        if numberAlreadyExist(hashed_number):
            print("skips the whole thing")
            return HttpResponse(f"Message successful")

        
        new_hashed_number = HashedNumber()
        new_hashed_number.hashed_number = hashed_number
        new_hashed_number.save()

        handleSendMessage({
            "body": getMessageBody(request_body["lang"]),
            "number": request_body["number"],
        })

        
        return HttpResponse(f"Message successful")


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

def cleanAndHashNumber(number):
    salt = os.environ["HASHING_SALT"]

    clean_number = re.sub(r'[^\w]', '', number)

    hashed_number = hashlib.sha256((clean_number + salt).encode()).hexdigest()
    
    return hashed_number

def numberAlreadyExist(number):
    is_number_in_store = HashedNumber.objects.filter(hashed_number=number)
    if is_number_in_store:
        return True
    
    return False

def handleSendMessage(message_info):
    messageHandler = SMSHandler(os.environ["TWILIO_ACCOUNT_SID"], os.environ["TWILIO_AUTH_TOKEN"])

    messageHandler.sendMessage({
    "number": message_info["number"],
    "body": message_info["body"]
    })

    