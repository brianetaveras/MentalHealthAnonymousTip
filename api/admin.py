from django.contrib import admin

# Register your models here.
from .models import TextMessage, HashedNumber

admin.site.register(TextMessage)
admin.site.register(HashedNumber)