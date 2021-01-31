from django.shortcuts import render
from django.http import JsonResponse
import json
from .utils import cookieCart,cartData
from .models import *
from .models import Customer
import datetime
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required




@login_required

def store(request):
		 data=cartData(request)

		 cartItems=data['cartItems']
		 order=data['order']
		 items=data['items'] 
		 products=Product.objects.all()
		 context = {'products':products,'cartItems':cartItems}
		 return render(request, 'store/store.html', context)

def cart(request):
         
	  	 data=cartData(request)

	  	 cartItems=data['cartItems']
	  	 order=data['order']
	  	 items=data['items']
	  	 context={'items':items,'order':order,'cartItems':cartItems}
	  	 return render(request, 'store/cart.html', context)


def checkout(request):
	     customer=Customer.objects.get(user=request.user)
	     data=cartData(request)

	     cartItems=data['cartItems']
	     order=data['order']
	     items=data['items']

	     context={'items':items,'order':order,'cartItems':cartItems,'customer':customer}
	     return render(request,'store/chuckout-r.html',context)

	   
def result(request):
		 order=Order.objects.all()
		 context={'order':order}
		 return render(request, 'store/result.html', context)
def show(request):
		 orderItem=OrderItem.objects.filter(order=12)
		 context={'orderItem':orderItem}
		 return render(request, 'store/hi.html', context)


		
def updateItem(request):
    
	 data=json.loads(request.body.decode('utf-8'))
	 productId=data['productId']
	 action =data['action']
	 customer=request.user.customer
	 product=Product.objects.get(id=productId)
	 order,created=Order.objects.get_or_create(customer=customer,complete=False)
	 orderItem,created=OrderItem.objects.get_or_create(order=order,product=product)
	 if  action=='add':
	 	 orderItem.quantity=( orderItem.quantity+1)
	 elif  action=='remove':
	 	 orderItem.quantity=( orderItem.quantity-1)
	 orderItem.save()
	 if orderItem.quantity<0:
	 	orderItem.delet()
	 return  JsonResponse('item was add',safe=False)
#from django.views.decorators.csrf import csrf_exempt
#@csrf_exempt
def process_order(request):
	
	transaction_id=datetime.datetime.now().timestamp()
	data=json.loads(request.body.decode('utf-8'))
	 
	if request.user.is_authenticated:

	 	customer=request.user.customer
	 	order,created=Order.objects.get_or_create(customer=customer,complete=False)
	
	else:
	 	     
	 	      print('cookies', request.session.set_test_cookie())

	 	     
	 	      name=data['form']
	 	      email=data['email']
	 	      cookieData=cookieCart(request)
	 	      items=cookieData['items']
	 	      customer=Customer.objects.create(email=email)
	 	      customer.name=name
	 	      customer.save()

	 	    
	 	      
	 	      order=Order.objects.create(customer=customer,complete=False)

	 	   


	 	      
	 	      for item in items :
	          	product=Product.objects.get(id=item['product']['id'])
	        

	          	orderItem=OrderItem.objects.create(product=product,order=order)
	          	
	          	

	          

	 

	ShippingAdress.objects.create(
	 		  	customer=customer,
	 		  	order=order,
	 		  	address=data['shipping']['address'],
	 		    city=data['shipping']['city'],
	 		
	 		    zipcode=data['shipping']['zipcode'],)







	return  JsonResponse('item was add',safe=False)
def send (request):
  return render(request,'store/contact.html')

    

