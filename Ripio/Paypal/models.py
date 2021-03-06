from django.db import models



class Product(models.Model):
    #ALL THE PRODUCTS 
	name = models.CharField(max_length=200)
	description = models.TextField(null=True, blank=True)
	image_url = models.ImageField(
     null=True, blank=True,upload_to="images")
	price = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.name


class Order(models.Model):
	product = models.ForeignKey(Product, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product