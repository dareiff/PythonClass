from django.db import models

# Create your models here.

class FamilyMembers(models.Model):
	member = models.CharField(max_length=100)
	def __unicode__(self):
		return self.member
	
class Photos(models.Model):
	name = models.CharField(max_length=100)
	imagefile = models.ImageField(upload_to='images/')
	taggedPeople = models.ManyToManyField(FamilyMembers)
	def __unicode__(self):
		return self.name