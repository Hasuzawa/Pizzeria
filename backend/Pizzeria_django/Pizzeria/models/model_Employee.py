from django.db import models
from django.db.models import Model, CharField, IntegerField

class Staff(Model):
    name = CharField(max_length=100)