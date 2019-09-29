from django.db import models

# Create your models here.

# Models of product categories

class Smart_Watch(models.Model):
  objects = models.Manager()
  image = models.ImageField(upload_to="product_images")
  name = models.CharField(max_length=200)
  category = models.CharField(max_length=300)
  slug = models.SlugField(max_length=50)
  sales_price = models.IntegerField()
  original_price = models.IntegerField()
  description = models.TextField(max_length=5000, null=True, blank=True)


class Essential_Oil(models.Model):
  objects = models.Manager()
  image = models.ImageField(upload_to="product_images")
  name = models.CharField(max_length=200)
  category = models.CharField(max_length=300)
  slug = models.SlugField(max_length=50)
  sales_price = models.IntegerField()
  original_price = models.IntegerField()
  description = models.TextField(max_length=5000, null=True, blank=True)


class Adult_Product(models.Model):
  objects = models.Manager()
  image = models.ImageField(upload_to="product_images")
  name = models.CharField(max_length=200)
  category = models.CharField(max_length=300)
  slug = models.SlugField(max_length=50)
  sales_price = models.IntegerField()
  original_price = models.IntegerField()
  description = models.TextField(max_length=5000, null=True, blank=True)