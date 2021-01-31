from django.db import models
from django.contrib.auth.models  import User

from django.db.models.signals import post_save
from django.core.signals import request_finished
from django.dispatch import receiver

class Profile(models.Model):
	 user=models.OneToOneField(User,null=True, blank=True,on_delete=models.CASCADE)
	 city=models.ForeignKey('City',related_name='user_city',on_delete=models.CASCADE ,null=True, blank=True)
	 phone_number=models.CharField(max_length=100)
	 
	 img=models.ImageField(upload_to='Profile/',null=True, blank=True)
	 @receiver(post_save,sender=User)
	 def create_user_profile(sender,instance,created,**kwargs):
	 	if created:
	 		Profile.objects.create(user=instance)
	 		
	 def __str__(self):
	 	   return str(self.user)

class City(models.Model):
	 
	 city=models.CharField(max_length=200)
	 phone_number=models.CharField(max_length=200)
	 img=models.ImageField(upload_to='Profile')
	 def __str__(self):
	 	   return   self.city
