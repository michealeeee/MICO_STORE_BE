from django.db import models
from mongoengine import Document, StringField,IntField

# Create your models here.
class User(Document):
    name = StringField
    age = IntField
    email = StringField
    
    