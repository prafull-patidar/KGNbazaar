from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name= 'Store'

urlpatterns = [
    path('',views.index,name='index'),
    path('shop/',views.shop,name='shop'),
    path('about/',views.about,name='about'),
    path('product_details/',views.product_details,name='product_details'),
    path('blog/',views.blog,name='blog'),
    path('<int:blog_id>/blog_details/',views.blog_details,name='blog_details'),
    path('cart/',views.cart,name='cart'),
    path('elements/',views.elements,name='elements'),
    path('confirmation/',views.confirmation,name='confirmation'),
    path('checkout/',views.checkout,name='checkout'),
    path('contact/',views.contact,name='contact'),
    path('NewestArrivals/',views.NewestArrivals,name='NewestArrivals'),
    path('SelectCurrency/',views.SelectCurrency,name='SelectCurrency'),
    path('PriceHighToLow/',views.PriceHighToLow,name='PriceHighToLow'),
    path('<int:product_id>/FavoriteItem/',views.FavoriteItem,name='FavoriteItem'),
    path('MostPopular/',views.MostPopular,name='MostPopular'),
    path('tracker/',views.tracker,name='tracker'),
    # path('<int:product_id>/AddToCart/',views.AddToCart,name='AddToCart'),
    # path('<int:product_id>/viewcart/',views.viewcart,name='viewcart'),
    # path('<int:product_id>/updatecart/',views.updatecart,name='updatecart'),
]