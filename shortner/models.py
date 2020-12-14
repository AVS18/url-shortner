from django.db import models
from django.contrib.auth.models import AbstractUser
class User(AbstractUser):
    limit = models.IntegerField(default=5)
    

class Url(models.Model):
    shorter_name = models.CharField(max_length=20,primary_key=True)
    original_link = models.CharField(max_length=2048)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    visitor = models.IntegerField(default=0)

class SiteAnnouncement(models.Model):
    message=models.CharField(max_length=2048)
    link_exist = models.BooleanField()
    link = models.CharField(max_length=2048,blank=True,null=True)