from django.db import models
from mongoengine import Document, StringField,IntField,EmailField,DateField

# Create your models here.
class User(Document):
    name = StringField()
    gender_ = StringField()
    email = EmailField()
    tel = StringField()
    password = StringField()
    DOR = DateField()