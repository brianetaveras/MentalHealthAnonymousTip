from django.db import models

# Create your models here.
class TextMessage(models.Model):
    language_code = models.CharField(max_length=3)
    message_body = models.TextField()

class HashedNumber(models.Model):
    hashed_number = models.CharField(max_length=64)