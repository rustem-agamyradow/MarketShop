from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def login(request):
    return render(request,'login.html')


def electronics(request):
    return render(request,'electronics.html')
# Create your views here.
