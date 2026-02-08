from django.db import models
from mongoengine import Document, StringField

# Create your models here.
class School(Document):
    name = StringField()
    address = StringField()
    country = StringField()
