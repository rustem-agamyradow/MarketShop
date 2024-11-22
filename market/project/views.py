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

def addproduct(request):
    return render(request,'addproduct.html')

def stock(request):
    return render(request,'stock.html')

def order(request):
    return render(request,'order.html')

def all_order(request):
    return render(request,'all_order.html')

def post_order(request):
    return render(request,'post_order.html')

def user_order(request):
    return render(request,'user_order.html')
