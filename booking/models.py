from django.db import models

class City(models.Model):
	name = models.CharField(max_length=140)
	
class Hotel(models.Model):
	name     = models.CharField(max_length=140)
	city     = models.ForeignKey(City)
	nr_rooms = models.IntegerField()
	price    = models.FloatField()

	class Meta:
		unique_together = ('name', 'city')

class Reservation(models.Model):
	first_name 	= models.CharField(max_length=140)
	last_name  	= models.CharField(max_length=140)
	phone      	= models.IntegerField()
	email 		= models.CharField(max_length=140)
	hotel_id 	= models.IntegerField()
	arrival 	= models.DateTimeField()
	departure 	= models.DateTimeField()
	total_rooms = models.IntegerField()
	total_cost  = models.FloatField()
