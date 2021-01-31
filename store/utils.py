import json
from .models import *
def cookieCart(request):
	try:
		  cart=json.loads(request.COOKIES['cart'])
	except:
        	  cart={}
        	  print('CART',cart)
	items=[]
	order={'get_cart_total':0,'get_cart_item':0}
	cartItems=order['get_cart_item']
	for  i in cart :

			try:
				 cartItems+=cart[i]["quantity"]
				 product=Product.objects.get(id=i)
				 total=(product.price*cart[i]["quantity"])
				 order['get_cart_total']+=total
				 order['get_cart_item']+=cart[i]["quantity"]
				 item={'product':{'id':product.id,
				 'name':product.name,
				 'price':product.price,
				  'imageURL':product.imageURL},

				  'quantity':cart[i]["quantity"],
				  'get_total':total
				  }
				 items.append(item)
				 if product.digital==False:
				 	order['shipping']=True
			except:
				 pass
	return {'items':items,'order':order,'cartItems':cartItems}


def cartData(request):
	if request.user.is_authenticated:
		customer=request.user.customer
		order,created=Order.objects.get_or_create(customer=customer,complete=False)
		items=order.orderitem_set.all()
		cartItems=order.get_cart_item

	else:
		
		 cookieData=cookieCart(request)

		 cartItems=cookieData['cartItems']
		 order=cookieData['order']
		 items=cookieData['items']
	return{'items':items,'order':order,'cartItems':cartItems}



def cookieCart(request):
	try:
		  cart=json.loads(request.COOKIES['cart'])
	except:
        	  cart={}
        	  print('CART',cart)
	items=[]
	order={'get_cart_total':0,'get_cart_item':0}
	cartItems=order['get_cart_item']
	for  i in cart :

			try:
				 cartItems+=cart[i]["quantity"]
				 product=Product.objects.get(id=i)
				 total=(product.price*cart[i]["quantity"])
				 order['get_cart_total']+=total
				 order['get_cart_item']+=cart[i]["quantity"]
				 item={'product':{'id':product.id,
				 'name':product.name,
				 'price':product.price,
				  'imageURL':product.imageURL},

				  'quantity':cart[i]["quantity"],
				  'get_total':total
				  }
				 items.append(item)
				 if product.digital==False:
				 	order['shipping']=True
			except:
				 pass
	return {'items':items,'order':order,'cartItems':cartItems}


def cartData(request):
	if request.user.is_authenticated:
		ss=request.user
		customer,created=Customer.objects.get_or_create(user=ss)
	
		order,created=Order.objects.get_or_create(customer=customer,complete=False)
		items=order.orderitem_set.all()
		cartItems=order.get_cart_item

	else:
		
		 cookieData=cookieCart(request)

		 cartItems=cookieData['cartItems']
		 order=cookieData['order']
		 items=cookieData['items']
	return{'items':items,'order':order,'cartItems':cartItems}


	 
