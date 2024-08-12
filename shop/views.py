from django.shortcuts import render
from .models import Post
# Create your views here.
def shop(request):
    return render(request, 'shop/shop.html')
def product(request):
    return render(request, 'product/product.html')
def home(request):
    return render(request, 'home/home.html')
def login(request):
    return render(request, 'login/login.html')
def cart(request):
    return render(request, 'cart/cart.html')
def shop(request):
    posts = Post.objects.all()
 
    return render(request, 'shop/shop.html',{'posts': posts})
