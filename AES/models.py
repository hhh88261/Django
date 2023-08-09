# Create your models here.
from django.db import models

class EncryptedData(models.Model):
    encrypted_data = models.TextField()