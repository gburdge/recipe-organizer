from django.contrib import admin
from models import *

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(IngredientCategory)
class MeasurementInline(admin.StackedInline):
    model = Measurement
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [MeasurementInline]


admin.site.register(Recipe, RecipeAdmin)