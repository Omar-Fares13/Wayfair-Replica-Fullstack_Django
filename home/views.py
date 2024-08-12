from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home/home.html')
def cart(request):
    return render(request, 'cart/cart.html')
def login(request):
    return render(request, 'login/login.html')
def App(request):
    return render(request, 'App/App.html')
def product(request):
    return render(request, 'product/product.html')
def shop(request):
    return render(request, 'shop/shop.html')
