from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price  = models.IntegerField(default=0)
    stock = models.IntegerField(default=0)
    # image
    image = models.ImageField(null=True, blank=True)