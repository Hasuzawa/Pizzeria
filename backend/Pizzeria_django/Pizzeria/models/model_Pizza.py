from django.db import models
from django.db.models import (Model, CharField, IntegerField, PositiveIntegerField, BooleanField, 
    DateTimeField, ForeignKey, ManyToManyField)

from datetime import datetime

#abstract base class
class PizzaElement(Model):
    #id
    name = CharField(max_length=127, default="")
    price = IntegerField(default=0)
    cost = IntegerField(default=0)
    src = CharField(max_length=127, blank=True, default="", verbose_name="image link")
    isActive = BooleanField(default=False,
        verbose_name="on sale ?",
        help_text="only active elements can be ordered. Has no effect on past orders.")

    description = CharField(max_length=511, blank=True, default="")
    unit_ordered = PositiveIntegerField(default=0)

    time_created = DateTimeField(auto_now_add=True, blank=True) #auto is exclsuive with default, blank is necessary for already created instances
    time_updated = DateTimeField(auto_now=True, blank=True)


    @classmethod
    def min_amount(self):
        return 0

    @classmethod
    def max_amount(self):
        return 0

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name}"


class Shape(PizzaElement):
    @classmethod
    def min_amount(self):
        return 1

    @classmethod
    def max_amount(self):
        return 1


class Sauce(PizzaElement):
    @classmethod
    def min_amount(self):
        return PositiveIntegerField(default=1)

    @classmethod
    def max_amount(self):
        return PositiveIntegerField(default=1)


class Topping(PizzaElement):
    pass


class Seasoning(PizzaElement):
    pass





class Pizza(Model):
    shape = ForeignKey(Shape, on_delete=models.DO_NOTHING, null=True)    #this is deliberate, it is suggested to never delete ingredients
    sauce = ForeignKey(Sauce, on_delete=models.DO_NOTHING, null=True)
    toppings = ManyToManyField(Topping)     
    seasonings = ManyToManyField(Seasoning)     



class PizzaPreset(Model):
    pass    # max topping and min topping are NOT enforced for PizzaPreset. It is assumed you know what you are doing when you add it youself.