from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'cart/cart.html')
def home(request):
    return render(request, 'home/home.html')
def login(request):
    return render(request, 'login/login.html')