from django.db import models
from django.db.models import Model, CharField, IntegerField


class Order(Model):
    #id
    name = CharField(max_length=127)