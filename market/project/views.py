from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')
# Create your views here.
