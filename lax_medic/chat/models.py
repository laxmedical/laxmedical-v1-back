from django.db import models
from    django.contrib.auth.models  import  User, Group

# Create your models here.

class SimpleTextMessage(models.Model):
    author      =   models.ForeignKey(User,related_name="simple_text_message_sents", on_delete=models.SET_NULL, null=True)
    to          =   models.ForeignKey(User, related_name="simple_text_message_receiveds", on_delete=models.SET_NULL, null=True) 
    message     =   models.TextField(null=False)
    message_code=   models.CharField(null=False, unique=True, max_length=50)
    date        =   models.DateTimeField(auto_now_add=True)
    is_received =   models.BooleanField(default=False)
    is_seen     =   models.BooleanField(default=False)
    is_deleted  =   models.BooleanField(default=False)

    def __str__(self):
        return  u"Message de {0}".format(self.author.username)

class GroupTextMessage(models.Model):
    author  =   models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    to      =   models.ForeignKey(Group, on_delete=models.SET_NULL, null=True) 
    message =   models.TextField(null=False)
    message_code=   models.IntegerField(null=False)
    date    =   models.DateTimeField(auto_now_add=True)
    received=   models.BooleanField(default=False)
    is_seen =   models.BooleanField(default=False)
    deleted =   models.BooleanField(default=False)

    def __str__(self):
        return  u"Message de {0}".format(self.author.username)
