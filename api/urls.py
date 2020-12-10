from django.urls import include, path
from .SMSController import SMSController
from django.views.generic import TemplateView


urlpatterns = [
    path('sendText/', SMSController.SMS, name="text-api"),
]