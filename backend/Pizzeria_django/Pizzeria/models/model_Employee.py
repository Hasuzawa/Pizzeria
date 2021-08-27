from django.db import models
from django.db.models import Model, CharField, IntegerField


class Employee(Model):
    name = CharField(max_length=127)
    role = CharField(max_length=127)
    salary = IntegerField(default=0)

    class Meta:
        abstract = True
    

class Manager(Employee):
    pass

class Staff(Employee):
    pass