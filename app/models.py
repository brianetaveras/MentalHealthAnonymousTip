from django.db import models

# Create your models here.
class ResourcesDocument(models.Model):
    country_code = models.CharField(max_length=3)
    resource_link = models.TextField()