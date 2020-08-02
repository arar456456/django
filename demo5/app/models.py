from django.db import models
from mongoengine import *

# Create your models here.
class Inmassage(Document):
    uid = SequenceField()
    name = StringField(max_length=30, required=True)
    habit = StringField(max_length=30)
