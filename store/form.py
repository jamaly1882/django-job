from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer


class CusForm(forms.Form):
	class Meta:
		  model=Customer
		  fields=['user','email']