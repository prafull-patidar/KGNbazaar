from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from Store.models import Products,Favorites,Orders,OrderUpdates,UserQuerrys,Blog
from useraccount.models import User,UserProfile
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import json


def index(request):
	products = Products.objects.all()
	return render(request,'index.html',{'products':products})

def shop(request):
	products = Products.objects.all()
	return render(request,'shop.html',{'products':products,})

def about(request):
	return render(request,'about.html')

def product_details(request):
	return render(request,'product_details.html')

def blog(request):
	blog = Blog.objects.all()
	return render(request,'blog.html',{'blog':blog})

def blog_details(request,blog_id):
	blog = get_object_or_404(Blog,pk=blog_id)
	return render(request,'blog_details.html',{'blog':blog})

def cart(request):
	return render(request,'cart.html')

def elements(request):
	return render(request,'elements.html')

def confirmation(request):
	order_id = request.session.get('order_id')
	email = request.session.get('email')
	orders = Orders.objects.filter(order_id=order_id,email=email)
	update = OrderUpdates.objects.filter(order_id=order_id)
	update_delievered = OrderUpdates.objects.filter(order_id = order_id)
	list_deliever = []
	for i in update_delievered:
		list_deliever.append(i.delievered)
	print(list_deliever)
	return render(request,'confirmation.html',{'order':orders,'update':update,'list_deliever':list_deliever})

def checkout(request):
	return render(request,'checkout.html')

def tracker(request):
	if request.method == "POST":
		order_id = request.POST.get('order_id')
		email = request.POST.get('email')

		try:
			order = Orders.objects.filter(order_id=order_id,email=email)
			if len(order)>0:
				update = OrderUpdates.objects.filter(order_id=order_id)
				updates = []
				delievered_list = []
				for i in update:
					delievered_list.append(i.delievered)

				if 'True' not in delievered_list:
					for item in update:
						updates.append({'text':item.update_desc,'time':item.update_timestamp.strftime("%d, %b %Y %H:%M:%S"),'delievered_list':delievered_list})
						response = json.dumps([updates,order[0].items_json],default=str)
				else:
					response = json.dumps({"order_delievered": "You don\'t have any placed order,check order id or email address."})
				return HttpResponse(response)
			else:
				print('else')
				return HttpResponse('{}')
		except Exception as e:
			print(e)
			return HttpResponse('{}')
	return render(request,'tracker.html')


def contact(request):
	thank = False
	if request.method == 'POST':
		querry = request.POST.get('querry')
		name = request.POST.get('name')
		email = request.POST.get('email')
		subject = request.POST.get('subject')
		UserQuerrys(querry=querry,name=name,email=email,subject=subject).save()
		thank=True
	return render(request,'contact.html',{'thank':thank})
	

def NewestArrivals(request):
	products = Products.objects.order_by('-pk')
	return render(request,'shop.html',{'products':products})

def SelectCurrency(request):
	currency = request.GET['currency']
	products = Products.objects.filter(currency__icontains=currency)
	return render(request,'shop.html',{'products':products})

def PriceHighToLow(request):
	products = Products.objects.order_by('-price')
	return render(request,'shop.html',{'products':products})

@login_required
def FavoriteItem(request,product_id):
	products = get_object_or_404(Products,product_id=product_id)
	user = request.user
	liked = Favorites.objects.filter(user = user,product=products).count()
	if not liked:
		fav = Favorites(user=user,product=products)
		fav.save()
		products.likes+=1
		products.save() 
	else:
		Favorites.objects.filter(user=user,product=products).delete()
		products.likes-=1
		products.save()
	return HttpResponseRedirect(reverse('Store:shop'))

def MostPopular(request):
	products = Products.objects.order_by('-likes')
	return render(request,'shop.html',{'products':products})

# def AddToCart(request,product_id):
# 	ip_address = request.META['REMOTE_ADDR']
# 	my_user = request.user
# 	products = Products.objects.get(product_id=product_id)
# 	try:
# 		user = User.objects.get(pk=my_user.pk)

# 		if user.is_authenticated:
# 			user_pk = user.pk
# 			user_profile_pk = user.userprofile.pk
# 			userprofile = UserProfile.objects.get(pk=user_profile_pk)
# 			TempAnonnymousUser.user = user
# 			TempAnonnymousUser.user_profile = userprofile
# 			TempAnonnymousUser.objects.create(ip_address=ip_address)
			
# 			cart = Cart.objects.create(user=user,ip_address = ip_address,product=products)
# 			cart.save()
# 			user.userprofile.cart_item = product_id
# 			user.save()
# 			messages.success(request,'Item added to cart successfull!')
# 			return HttpResponseRedirect(reverse('Store:viewcart',args=(product_id,)))
			
# 	except User.DoesNotExist:
# 		# UserProfile(cart_item=product_id).save()
# 		TempAnonnymousUser(ip_address=ip_address).save()
# 		messages.success(request,'Item added to cart successfully!')
# 		return HttpResponseRedirect(reverse('Store:viewcart',args=(product_id,)))

# def viewcart(request,product_id):
# 	user = request.user
# 	products = Products.objects.get(product_id=product_id)
# 	if user.is_authenticated:
# 		Cart.user = user
# 		Cart.product = products
# 		cart = Cart(ip_address=request.META['REMOTE_ADDR'])
# 		cart.save()
# 		print(cart.product.product_name)
# 		print(cart.user.email)
# 		products = Products.objects.filter(product_id=product_id)
# 		return render(request,'cart.html',{'cart':cart,'products':products})
# 	else:
# 		Cart.product = products
# 		cart = Cart(ip_address=request.META['REMOTE_ADDR'])
# 		cart.save()
# 		print(cart.product.product_name)
# 		print('hello')
# 		products = Products.objects.filter(product_id=product_id)
# 		return render(request,'cart.html',{'cart':cart})

# def updatecart(request,product_id):
# 	user = request.user
# 	print(user.email)
# 	return HttpResponseRedirect(reverse('Store:viewcart',args=(product_id,)))