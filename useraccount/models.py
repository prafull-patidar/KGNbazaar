# from django.contrib.auth.models import (
#     AbstractBaseUser, PermissionsMixin, BaseUserManager,
# )
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser,BaseUserManager
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator

from django.db.models.signals import post_save
from django.dispatch import receiver

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

class UserManager(BaseUserManager):

	use_in_migrations = True

	def _create_user(self, email, password, **extra_fields):
		if not email:
			raise ValueError('The given email must be set')
		email = self.normalize_email(email)
		user = self.model(email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', False)
		extra_fields.setdefault('is_superuser', False)
		return self._create_user(email, password, **extra_fields)

	def create_superuser(self, email, password, **extra_fields):
		extra_fields.setdefault('is_staff', True) 
		extra_fields.setdefault('is_superuser', True)

		if extra_fields.get('is_staff') is not True:
			raise ValueError('Superuser must have is_staff=True.')
		if extra_fields.get('is_superuser') is not True:
			raise ValueError('Superuser must have is_superuser=True.')
		return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
	
	REQUIRED_FIELDS = []

	email = models.EmailField(verbose_name=_("email address"), unique=True,blank=False,error_messages={'unique': _("A user is already registered with this email address"),},)
	# username =models.CharField(verbose_name=_('user_name'),max_length=20,blank=True)
	first_name = models.CharField(_('first name'),max_length=30,blank=True,)
	last_name = models.CharField( _('last name'),max_length=150,blank=True,)
	is_staff = models.BooleanField(_('staff status'),default=False,help_text=_('Designates whether the user can log into ''this admin site.'),)
	is_active = models.BooleanField(_('active'),default=True,help_text=_('Designates whether this user should be ''treated as active. Unselect this instead ''of deleting accounts.'),)
	date_joined = models.DateTimeField( _('date joined'),default=timezone.now,)
	objects = UserManager()
	USERNAME_FIELD ='email'

class UserProfile(models.Model):
	phone_number = models.CharField(_('phone number'),max_length=15,validators=[phone_regex],blank=True)
	company_name = models.CharField(_('comapny name'),max_length=50,blank=True)
	address1 = models.CharField(_('address line 01'),max_length=400,blank=True)
	address2 = models.CharField(_('address line 02'),max_length=400,blank=True)
	country = models.CharField(_('country'),max_length=50,blank=True)
	town = models.CharField(_('town'),max_length=80,blank=True)
	district = models.CharField(_('district'),max_length=80,blank=True)
	state = models.CharField(max_length=100,blank=True,default='')
	postcode = models.CharField(_('postcode/zipcode'),max_length=100,default='',blank=True,null=True)
	items_json = models.CharField(max_length=5000,default='')
	amount = models.DecimalField(max_digits=30,decimal_places=2,default=0)
	user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)

	class Meta:
		db_table = 'UserProfile'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
