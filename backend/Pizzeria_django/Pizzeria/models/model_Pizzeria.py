from django.db import models
from django.db.models import Model, CharField, IntegerField

# Create your models here.
class Pizzeria(Model):
    #id
    name = CharField(max_length=127, default="")
