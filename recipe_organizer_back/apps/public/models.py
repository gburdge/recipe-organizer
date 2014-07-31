from django.db import models

# Create your models here, i.e.: #photo, ingredients, description, instructions, prep time, total time, tags, favorited


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(default="To be done later.")
    ingredients = models.ManyToManyField('Ingredient', null=True, blank=True, through="Measurement")

    Directions = models.TextField(default="To be done later.")
    image = models.CharField(max_length=500, default="no image")

    def __unicode__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class IngredientCategory(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Ingredient categories"

    def __unicode__(self):
        return self.name


class Measurement(models.Model):
    amount = models.CharField(max_length=50)
    recipe = models.ForeignKey("Recipe")
    ingredient = models.ForeignKey('Ingredient')

    def __unicode__(self):
        return self.amount