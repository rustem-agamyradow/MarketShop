from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.product,name='product'),
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('electronics',views.electronics,name='electronics'),
    path('about',views.about,name='about'),
    path('checkout',views.checkout,name='checkout'),

]