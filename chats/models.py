from django.db import models


# Create your models here.
class Chats(models.Model):
    chat_name = models.CharField(max_length=30)
    chat_description = models.TextField()
    creation_date = models.DateField()
    chat_icon = models.URLField()


class User(models.Model):
    user_name = models.CharField(max_length=30)
    bio = models.TextField()
    register_date = models.DateField()
    user_icon = models.URLField()
    chats = models.ManyToManyField(Chats)
