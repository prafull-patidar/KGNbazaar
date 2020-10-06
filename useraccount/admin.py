from django.contrib import admin
from django.contrib.auth import get_user_model
from useraccount.models import User,UserProfile
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.db import models



class CustomUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields' : ('email','password')}),
		(_('Personal Info'),{'fields' : ('first_name','last_name')}),
		(_('Permissions'),{'fields' : ('is_active','is_staff','is_superuser','groups','user_permissions')}),
		(_('Important Dates'),{'fields' : ('last_login','date_joined')}),
	)

	add_fieldsets = (
		(None, {
			'classes':('wide',),
			'fields':('email','password'),
		}),
	)
	list_display = ('email','first_name','last_name','is_active','is_staff')
	search_fields = ('email','first_name','last_name')
	list_display_links = ('email','first_name','last_name')
	ordering =('email',)
	list_filter = ['email','is_staff']

class CustomUserProfileAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {'fields' : ('user_id','phone_number','country','company_name','postcode','town','district','address1','address2')}),
		)

	list_display = ('user_id','phone_number','country','company_name','postcode','town','district','address1')
	search_fields = ('phone_number','country','company_name','postcode','town','district')
	list_display_links = ('phone_number','country','company_name','postcode','town','district')
	ordering =('country','district')
	list_filter = ['country','district','town']


admin.site.register(get_user_model(),CustomUserAdmin)
admin.site.register(UserProfile,CustomUserProfileAdmin)

