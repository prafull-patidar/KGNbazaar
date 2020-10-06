from django.contrib import admin
from Store.models import Products,Favorites,Orders,OrderUpdates,UserQuerrys,Blog
# Register your models here.

class CustomProducts(admin.ModelAdmin):
	list_display = ('product_name','category','product_details','currency','price','likes')
	search_fields = ('product_name','category','price','product_details','currency')
	list_display_links = ('product_name','category','product_details','currency','price')
	ordering=('product_id',)
	list_filter = ['product_name','category','currency']


class CustUserQuerrys(admin.ModelAdmin):
	list_display = ('name','subject','email')
	search_fields = ('subject','querry')
	list_display_links = ('name','subject','email')
	list_filter = ['subject']


class CustomOrders(admin.ModelAdmin):
	fieldsets = (
		(None, {'fields' : ('user_id',)}),
		)
	list_display = ('user_id','order_id','items_json','amount')
admin.site.register(Products,CustomProducts)
admin.site.register(Favorites)
admin.site.register(Orders)
admin.site.register(OrderUpdates)
admin.site.register(UserQuerrys,CustUserQuerrys)
admin.site.register(Blog)