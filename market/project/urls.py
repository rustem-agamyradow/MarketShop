from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('logout/',views.logoutView,name='logout'),
    path('login/',views.loginView,name='login'),
    path('register/',views.registerView,name='register'),   
    path('electronics',views.electronics,name='electronics'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout,name='checkout'),
    path('wishlist',views.wishlist,name='wishlist'),
    path('search',views.search,name='search'),
    path('contact',views.contact,name='contact'),
    path('cart',views.cart,name='cart'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('stock',views.stock,name='stock'),
    path('order',views.order,name='order'),
    path('all_order',views.all_order,name='all_order'),
    path('user_order',views.user_order,name='user_order'),
    path('post_order',views.post_order,name='post_order'),


]