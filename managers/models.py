from django.db import models
from datetime import datetime


class Manager(models.Model):
    name = models.CharField(max_length =200)
    photo = models.ImageField(blank = True, upload_to='photos/%Y/%m/%d/')
    designation = models.CharField(max_length=200)
    description = models.TextField(blank = True)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    is_available = models.BooleanField(default=True)
    hire_date = models.DateTimeField(default = datetime.now)

    def __str__(self):
        return f"{self.name} is a {self.designation}"

class Worker(models.Model):

    designation = [
        ('Plumber',('Efficient in Plumbing work')),
        ('electrician',('Efficient in handling electircal work')),
        ('House_maid',('For household activities')),
    ]

    name = models.CharField(max_length=200)
    work = models.CharField(max_length=200,choices=designation,default='House_maid')
    manager = models.ForeignKey(Manager, on_delete=models.DO_NOTHING)
    address = models.TextField()
    phone = models.CharField(max_length=20)
    is_availabe = models.BooleanField(default=True)
    hire_date  = models.DateTimeField(default = datetime.now)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return f"{self.name} is a {self.work}"
