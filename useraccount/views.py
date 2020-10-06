from django.shortcuts import render,redirect,get_object_or_404
# from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import get_user_model 
from django.core.mail import EmailMessage
from .models import User,UserProfile
from django.contrib.auth import login,authenticate,logout
from django.views import View
from django.urls import reverse
import re
# from useraccount.forms import CustomPasswordResetForm
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .utils import token_generator
from django.contrib.auth.decorators import login_required
from Store.models import Orders,OrderUpdates,Products
from django.contrib.auth.hashers import make_password
import datetime
from django.utils import timezone
from datetime import timedelta
# Create your views here.
from Store import views
import json
from django.views.decorators.csrf import csrf_exempt


def profile(request):
	products = Products.objects.all()
	user = request.user
	if user.is_authenticated:
		return render(request,'profile.html',{'products':products})
	else:
		email = request.POST.get('email')
		password = request.POST.get('password')
	try:
		my_user =User.objects.get(email=email)
			
		if my_user.is_active:
			user = authenticate(email=email,password=password)
			if user is not None:
				login(request,user)
				return render(request,'profile.html',{'products':products})
			else:
				messages.error(request,'Incorrect Email or Password!')
				return redirect('useraccount:login')
		else:
			messages.error(request,'Please varify your email first!')
			return redirect('useraccount:login')
	except User.DoesNotExist:
		messages.error(request,'Invalid Email! you didn\'t signup')
		return redirect('useraccount:login')
	

def signup(request):
	if request.method == 'POST':
		first_name = request.POST.get('firstname')
		last_name = request.POST.get('lastname')
		email =  request.POST.get('email')
		password =  request.POST.get('password')
		if not User.objects.filter(email=email).exists(): 
			user = User(email=email,first_name=first_name,last_name=last_name)
			user.set_password(password)
			user.is_active = False
			user.save()

			uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
			domain = get_current_site(request).domain
			link = reverse('useraccount:activate',kwargs={'uidb64':uidb64,'token':token_generator.make_token(user)})
			activate_url = 'http://'+domain+link
			email_subject = 'KGNbazaar Email Confirmation'
			email_body = 'Hi ' + user.first_name + ' ' + user.last_name + '!, Please click on below link to varify!\n' + activate_url 
			email = EmailMessage(
					email_subject,
					email_body,
					'noreply@KGNbazaar.com',
					[email],
					)
			email.send(fail_silently = False)
		else:
			return HttpResponse('This email already exists.')
		messages.info(request,'Please check your mails , we have sent you a varification link.')
		return redirect('useraccount:login')
	else:
		ip = request.session.get('ip_address')
		print(ip)
		return render(request, 'signup.html')
 
class VarificationView(View):
	def get(self,request,uidb64,token):

		try:
			user_id = urlsafe_base64_decode(force_text(uidb64))
			user = User.objects.get(pk=user_id)

			if not token_generator.check_token(user,token):
				return redirect('useraccount:login')

			if user.is_active:
				return redirect('useraccount:login')

			user.is_active=True
			user.save()
			messages.success(request, 'Hi ' + user.first_name + ' ' + user.last_name + ', Your account has been created successfully!')
			return redirect('useraccount:login')
		except Exception as e:
			return HttpResponse('email varification failed!')

		return redirect('useraccount:login')


def logout_view(request):
	request.session.flush()
	logout(request)
	messages.success(request,'You are logged out!')
	return redirect('useraccount:login')

def saveuserdetails(request):
	user = request.user
	if request.method == 'POST':
		company_name = request.POST.get('company_name','')
		phone_number = request.POST.get('phone_number','')
		address1 = request.POST.get('address1','')
		address2 = request.POST.get('address2','')
		town = request.POST.get('town','')
		district = request.POST.get('district','')
		state = request.POST.get('state','')
		country = request.POST.get('country','')
		postcode = request.POST.get('zip_code','')
		UserProfile.objects.filter(user_id=user.pk).update(company_name=company_name,phone_number=phone_number,address1=address1,address2=address2,town=town,district=district,state=state,country=country,postcode=postcode)
		
		return redirect('useraccount:profile')
	return redirect('useraccount:profile')
		
def edituserdetails(request):
	user = request.user
	if request.method == 'POST':
		company_name = request.POST.get('company_name','')
		phone_number = request.POST.get('phone_number','')
		address1 = request.POST.get('address1','')
		address2 = request.POST.get('address2','')
		town = request.POST.get('town','')
		district = request.POST.get('district','')
		state = request.POST.get('state','')
		country = request.POST.get('country','')
		postcode = request.POST.get('zip_code','')
		if company_name == '':
			company_name = user.userprofile.company_name
		if phone_number == '':
			phone_number = user.userprofile.phone_number
		if address1 == '':
			address1 = user.userprofile.address1
		if address2 == '':
			address2 = user.userprofile.address2
		if town == '':
			town = user.userprofile.town
		if district == '':
			district = user.userprofile.district
		if state == '':
			state = user.userprofile.state
		if country == '':
			country = user.userprofile.country
		if postcode == '':
			postcode = user.userprofile.postcode
		UserProfile.objects.filter(user_id=user.pk).update(company_name=company_name,phone_number=phone_number,address1=address1,address2=address2,town=town,district=district,state=state,country=country,postcode=postcode)
		
		return redirect('useraccount:profile')
	return redirect('useraccount:profile')

def payment(request):
	user=request.user
	thank = False
	if request.method == 'POST':
		payment_method = request.POST.get('payment_method','')
		items_json = request.POST.get('itemsJson')
		amount = request.POST.get('amount')
		amount=float(amount)
		order = Orders(user_id=user.pk,payment_method=payment_method,items_json=items_json,amount=amount)
		order.save()
		update = OrderUpdates(order_id=order.pk,update_desc='Your Order is successfully Placed.',update_timestamp=datetime.datetime.now().strftime('%b, %M %Y  %H:%M:%S'))
		update.save()
		thank = True
		if order.payment_method == 'COD':
			return render(request,'profile.html',{'thank':thank})
		else:
			param_dict = {
			'MID':'WorldP64425807474247',
			'ORDER_ID':order.order_id,
			'TXN_AMOUNT':'1',
			'CUST_ID':user.email,
			'INDUSTRY_TYPE_ID':'Retail',
			'WEBSITE':'WEBSTAGING',
			'CHANNEL_ID':'WEB',
			'CALLBACK_URL':'http://localhost:8000/handlerequest/',
			}
			mid = param_dict['MID']
			orderid = param_dict['ORDER_ID']
			timestamp = timezone.now()
			return render(request,'paytm.html',{'param_dict':param_dict,'mid':mid,'orderid':orderid,'timestamp':timestamp})

	return redirect('useraccount:profile')

def UserOrders(request,user_pk):
	user = request.user
	orders = user.orders_set.all()
	# items_not_delievered = user.orders_set.filter(delievered=False)
	# items_delievered = user.orders_set.filter(delievered=True)
	return render(request,'profile.html',{'orders':orders})

def userorderdetails(request,order_id):
	order = get_object_or_404(Orders,pk=order_id)
	update = OrderUpdates.objects.filter(order_id=order_id)
	return render(request,'Orderdetails.html',{'order':order,'update':update})

@csrf_exempt
def handlerequest(request):
	return HttpResponse('done')