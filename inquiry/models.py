from django.db import models
from datetime import datetime

class Inquiry(models.Model):
    issue = models.CharField(max_length=150)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=200)
    flat = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(default=datetime.now)
    user_id = models.IntegerField() 
    resolve = models.BooleanField(default=False)

    def __str__(self):
        return self.name
