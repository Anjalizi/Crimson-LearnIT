from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

class skintype(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	image = models.CharField(max_length=1000)

	def __str__(self):
		return self.name

class undertone(models.Model):
	category = models.CharField(max_length=30, default='Fill')
	image_u = models.CharField(max_length=1000)
	vein_color = models.CharField(max_length=100)
	jewellery = models.CharField(max_length = 100)

	def __str__(self):
		return self.category

class contactpage(models.Model):
    suggestion = models.TextField(max_length=200, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=30)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone = models.CharField(null=True,validators=[phone_regex], max_length=17) # validators should be a list

    def __str__(self):
    	return self.created_by


