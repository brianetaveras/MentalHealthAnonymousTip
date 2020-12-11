from django.urls import include, path
from .SMSController import SMS
from django.views.generic import TemplateView


urlpatterns = [
    path('sendText/', SMS, name="text-api"),
]