from django.urls import path

from . import views
app_name='accounts'

urlpatterns = [
	#Leave as empty string for base url
	path('profile/', views.profile,name='profile'),
	path('signup', views.Signup,name='signup'),
	
	path('profile/edite', views.profile_edite,name='profile/edite'),


	]