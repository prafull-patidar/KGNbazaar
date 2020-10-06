from django.db import models
from django.utils import timezone
import datetime 
from useraccount.models import User,UserProfile
from django.core.validators import RegexValidator
from django.utils.translation import ugettext_lazy as _
# Create your models here.
phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
currency_choices = (('₹','₹'),('$','$'),('€','€'))
category_choices = (('watch','watch'),('mobile','mobile'),('bag','bag'),('jwellery','jwellery'),('mens clothes','mens clothes'),('womens wear','womens wear'))
delievered_choices = (('True','True'),('False','False'))
order_placed = (('True','True'),('False','False'))

class Products(models.Model):
	product_id = models.IntegerField(primary_key=True)
	product_name = models.CharField(max_length=250)
	product_details = models.CharField(max_length=1200)
	category = models.CharField(max_length=100,default='watch',choices=category_choices)
	product_image = models.ImageField(upload_to='product_image/')
	currency = models.CharField(max_length=10,default='₹',choices=currency_choices)
	price = models.IntegerField()
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.product_name

class Favorites(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	product = models.ForeignKey(Products,on_delete=models.CASCADE)

class Orders(models.Model):
	order_id = models.AutoField(primary_key=True)
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	items_json = models.CharField(max_length=5000,default='')
	payment_method = models.CharField(max_length=30,default='')
	amount = models.DecimalField(max_digits=30,decimal_places=2,default=0)

	def __str__(self):
		return self.items_json

class OrderUpdates(models.Model):
	update_id = models.AutoField(primary_key=True)
	order_id = models.IntegerField(default='')
	update_desc = models.CharField(max_length=5000)
	update_timestamp = models.DateTimeField(auto_now_add=True)
	delievered = models.CharField(max_length=20,default=False,choices=delievered_choices)
	order_placed = models.CharField(max_length=20,default=False,choices=order_placed)

	def __str__(self):
		return self.update_desc[0:50] + '...'

class UserQuerrys(models.Model):
	querry = models.CharField(max_length=5000)
	name = models.CharField(max_length=100)
	email=models.EmailField()
	subject = models.CharField(max_length=500)

	def __str__(self):
		return self.subject[0:100] + '...'

class Blog(models.Model):
	title = models.CharField(max_length=1000)
	blog_desc = models.CharField(max_length=10000)
	blog_desc_note = models.CharField(max_length=8000)
	blog_img = models.ImageField(upload_to='blog_images/')
	blog_upload_date = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=100,default='')
	author_desc = models.CharField(max_length=1000,default='')
	author_img = models.ImageField(upload_to='blog_author_img/')

	def __str__(self):
		return self.title