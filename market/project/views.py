from django.shortcuts import render,redirect
from . forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

def logoutView(request):
    logout(request)
    return redirect('home')

def loginView(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username = username,password = password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                
                else:
                    messages.info(request,'Disabled Account')
            
            else:
                messages.info(request,'Check your username and password')

    else:
        form = LoginForm()

    return render(request,'login.html',{'form':form})






def registerView(request):
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created, You can login')
            return redirect('login')
        
    else:
        form = RegisterForm()
        

    return render(request,'register.html',{'form':form})

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
