from django.urls import path, include
from .views import VarificationView#,ResetVarificationEmailView
from . import views
from django.contrib.auth import views as auth_views
from django.views.decorators.csrf import csrf_exempt
from KGNbazaar import settings
from django.conf.urls.static import static
app_name= 'useraccount'

urlpatterns = [
	path('accounts/', include('allauth.urls')),
	path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
	path('signup/',views.signup,name='signup'),
	path('activate/<uidb64>/<token>/',VarificationView.as_view(),name='activate'),
	path('profile/',views.profile,name='profile'),
	path('logout/',views.logout_view,name='logout'),
	path('saveuserdetails/',views.saveuserdetails,name='saveuserdetails'),
	path('edituserdetails/',views.edituserdetails,name='edituserdetails'),
	path('payment/',views.payment,name='payment'),
	path('<int:user_pk>/UserOrders/',views.UserOrders,name='UserOrders'),
	path('<int:order_id>/userorderdetails/',views.userorderdetails,name='userorderdetails'),
	path('handlerequest/',views.handlerequest,name='handlerequest'),
]

urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)


# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']

 	# path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
  #   path('password_change/done/', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
  
    # path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),