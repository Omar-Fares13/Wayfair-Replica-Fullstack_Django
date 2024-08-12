from django.shortcuts import render

# Create your views here.
def checkout(request):
    return render(request, 'checkout/checkout.html')
def home(request):
    return render(request, 'home/home.html')
def login(request):
    return render(request, 'login/login.html')