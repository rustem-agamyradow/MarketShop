from django.shortcuts import render


def home(request):
    return render(request,'index.html')

def product(request):
    return render(request,'product.html')

# Create your views here.
