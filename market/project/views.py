from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def login(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def electronics(request):
    return render(request,'electronics.html')


def about(request):
    return render(request,'about.html')


def checkout(request):
    return render(request,'checkout.html')
# Create your views here.
