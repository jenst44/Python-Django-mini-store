from django.db import models

class Product(models.Model):
	brand = models.TextField()
	product_name = models.TextField()
	price = models.TextField()
	description = models.TextField()
	created_at = models.DateField()
