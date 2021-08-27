from django.contrib import admin
from django.contrib.admin import ModelAdmin

from django import forms
from django.forms import ModelForm

from .models.model_Pizzeria import Pizzeria
from .models.model_Pizza import Pizza, Shape, Sauce, Topping, Seasoning
from .models.model_Employee import Manager, Staff

#ModelForm controls how the inerface new instances look and can be created

class ShapeModelForm(ModelForm):
    class Meta:
        fields = "__all__"
        model = Shape



#ModelAdmin controls how the model looks in table form

class PizzaElementAdmin(ModelAdmin):
    list_display = ("name", "isActive", "price", "cost", "unit_ordered", "time_updated", "time_created", "min_amount")

class ShapeAdmin(PizzaElementAdmin):
    pass

class SauceAdmin(PizzaElementAdmin):
    pass

class ToppingAdmin(PizzaElementAdmin):
    pass

class SeasoningAdmin(PizzaElementAdmin):
    pass


# register on admin site

admin.site.register(Pizzeria)
admin.site.register(Pizza)
admin.site.register(Shape, ShapeAdmin)
admin.site.register(Sauce, SauceAdmin)
admin.site.register(Topping, ToppingAdmin)
admin.site.register(Seasoning, SeasoningAdmin)
#admin.site.register(Manager)
#admin.site.register(Staff)

# presets: Margherita, 