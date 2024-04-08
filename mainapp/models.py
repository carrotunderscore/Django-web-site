from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Cat(models.Model):
    id_cat = models.CharField(max_length=200, primary_key=True)
    url = models.URLField(max_length=200)
    breed = models.CharField(max_length=100, default="null")
    width = models.IntegerField(default=400)
    height = models.IntegerField(default=500)
    name = models.URLField(default="null", max_length=200)
    rating = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return f"Cat: {self.id_cat} - {self.breed}"





