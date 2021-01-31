from django.urls import path,include

from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.send_m, name='send_m'),
	]