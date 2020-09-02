from django.db import models
import datetime
from django.utils import timezone


class Customer(models.Model):
		name = models.CharField(max_length=200, null=True)
		contact_number = models.CharField(max_length=200, null=True)
		email = models.CharField(max_length=200, null=True)
		Address = models.CharField(max_length=200, null=True)
		date_created = models.DateTimeField(auto_now_add=True, null=True)


		def __str__(self):            
			return self.name        

class Tag(models.Model):
		name = models.CharField(max_length=200, null=True)

		def __str__(self):
			return self.name 
			

class Meal(models.Model):
		NAME = (
				('Fried Rice', 'Fried Rice'),
				('Kottu', 'Kottu'),
				('Pizza', 'Pizza'),
				('Hoppers', 'Hoppers'), 
				('Shorties', 'Shorties'),
				('Rice&Curry', 'Rice&Curry'),
				
				) 
		price = models.FloatField(null=True)
		name = models.CharField(max_length=200, null=True, choices=NAME)
		
		description = models.CharField(max_length=200, null=True)
		tags = models.ManyToManyField(Tag)
	
		def __str__(self):            
			return self.name     

class Order(models.Model):
		STATUS = (
				('Pending', 'Pending'),
				('Out for delivery', 'Out for delivery'),
				('Delivered', 'Delivered'),
				)

		customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
		meal = models.ForeignKey(Meal, null=True, on_delete= models.SET_NULL)
		date_created = models.DateTimeField(auto_now_add=True, null=True)
		status = models.CharField(max_length=200, null=True, choices=STATUS)
 