from django.db import models
from django.db.models import Model, CharField, IntegerField

#abstract base class
class PizzaElement(Model):
    #id
    name = CharField(max_length=127, default="")
    price = IntegerField(default=0)
    src = CharField(max_length=127, default="")



    @classmethod
    def min_amount():
        return 0

    @classmethod
    def max_amount():
        return 0

    class Meta:
        abstract = True


class Pizza(Model):
    pass


class Shape(PizzaElement):
    #SHAPE_CHOICES = [(0, "round"), (1, "square")]
    pass


class Sauce(PizzaElement):
    pass


class Topping(PizzaElement):
    pass


class Ingredient(PizzaElement):
    pass