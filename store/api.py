from .models import  Order
from .serializers import OrderSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view




@api_view(['GET'])
def shp_list_api(request):
	shipe=Order.objects.all()
	data=OrderSerializer(shipe ,many=True).data
	return Response({'data':data})
@api_view(['GET'])
def select_one_api(request,id):
	select=Order.objects.get(transaction_id=id)
	data=OrderSerializer(select).data
	return Response({'data':data})
class  Order_list_api (generics.ListAPIView):
	
	queryset=Order.objects.all()
	serializer_class=OrderSerializer
class  Order_list_api_all_opretion(generics.RetrieveUpdateDestroyAPIView):
	
	queryset=Order.objects.all()
	serializer_class=OrderSerializer
	lookup_field='transaction_id'
class  Order_creat_api (generics.ListCreateAPIView):
	
	queryset=Order.objects.all()
	serializer_class=OrderSerializer





