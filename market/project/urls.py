from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('product',views.home,name='product'),
    path('login',views.login,name='login'),

]