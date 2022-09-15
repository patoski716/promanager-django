from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.

CHOICES_STATUS = (
        ('COMPLETED', 'Completed'),
        ('IN PROGRESS', 'In Progress'),
        ('NOT STARTED', 'Not Started'),

)

class Client(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    phone=models.CharField(max_length=50)
    created_by = models.ForeignKey(User, related_name='clients', on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Project(models.Model):
    title=models.CharField(max_length=500)
    description=models.TextField()
    status=models.CharField(max_length=200,choices=CHOICES_STATUS, default='COMPLETED')
    client = models.ForeignKey(Client, related_name='projects', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title