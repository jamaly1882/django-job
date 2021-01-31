from django.urls import path,include
from . import api
from . import views

urlpatterns = [
	#Leave as empty string for base url
	path('', views.store, name='store'),
	path('cart/', views.cart, name='cart'),
	path('checkout/', views.checkout, name='checkout'),
	path('updateItem/', views.updateItem, name="updateItem"),
	path('process_order/', views.process_order, name="process_order"),
	path('result/', views.result, name="result"),
	path('show/', views.show, name="show"),
	

	path('api/order',api.shp_list_api, name="shp_list_api"),
	path('api/order/<int:id>',api.select_one_api, name="shplistapi"),
	path('api/v2/order/',api.Order_list_api.as_view(),name='Order_list_api'),

	path('api/v2/order/<int:transaction_id>',api.Order_list_api_all_opretion.as_view(),name='Order_list_api_all_opretion'),
	path('api/v2/order/p',api.Order_creat_api.as_view(),name='Order_creat_api'),





]