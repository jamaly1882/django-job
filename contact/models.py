from django.db import models

class Info(models.Model):
	place=models.CharField(max_length=100)
	phone_number=models.CharField(max_length=100)
	email=models.EmailField(max_length=254)
	class Meta:
		verbose_name=("info")
		verbose_name_plural=("infos")
