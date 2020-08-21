from django.db import models

# Create your models here.
class contacts(models.Model):
    id = models.CharField(max_length=100,primary_key=True)
    name = models.CharField(max_length=100,default="")
    company = models.CharField(max_length=100,default="")
    emails = models.CharField(max_length=100,default="")
    phones = models.CharField(max_length=100,default="")
    matching_terms = models.CharField(max_length=100,default="")
    last_contact = models.CharField(max_length=100,default="")

class dropbox(models.Model):
    id = models.IntegerField(primary_key=True)
    path = models.CharField(max_length=100,default="")
    title = models.CharField(max_length=100,default="")
    shared_with = models.CharField(max_length=100,default="")
    matching_terms = models.CharField(max_length=100,default="")
    created = models.CharField(max_length=100,default="")


class slack(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    channel = models.CharField(max_length=100, default="")
    author = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=100, default="")
    time_stamp = models.CharField(max_length=100, default="")
    matching_terms = models.CharField(max_length=100, default="")


class tweet(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True)
    user = models.CharField(max_length=100, default="")
    message = models.CharField(max_length=100, default="")
    time_stamp = models.CharField(max_length=100, default="")
    matching_terms = models.CharField(max_length=100, default="")