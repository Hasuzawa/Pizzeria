from django.contrib import admin

from .models.model_Pizzeria import Pizzeria
from .models.model_Pizza import Pizza, Shape, Sauce, Topping
from .models.model_Employee import Staff

admin.site.register(Pizzeria)
admin.site.register(Pizza)
admin.site.register(Shape)
admin.site.register(Sauce)
admin.site.register(Topping)
admin.site.register(Staff)