from django.db import models
from django.contrib.auth.models import User

class skintype(models.Model):
	name = models.CharField(max_length=30, unique=True)
	description = models.CharField(max_length=100)
	image = models.ImageField(max_length=100, default='vol5-4.png')

	def __str__(self):
		return self.name

class undertone(models.Model):
	vein_color = models.CharField(max_length=30)
	jewellery = models.CharField(max_length = 30)
	skintone = models.ForeignKey(skintype, related_name='utones')

class contactpage(models.Model):
    suggestion = models.TextField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='cpages')
    phone = models.IntegerField()

