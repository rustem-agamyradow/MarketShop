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

def register(request):
    return render(request,'register.html')

def electronics(request):
    return render(request,'electronics.html')


def about(request):
    return render(request,'about.html')


def checkout(request):
    return render(request,'checkout.html')


def wishlist(request):
    return render(request,'wishlist.html')


def search(request):
    return render(request,'search.html')


def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'cart.html')
# Create your views here.
