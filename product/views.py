from django.shortcuts import render
from .models import Post
# Create your views here.
def product(request):
    return render(request, 'product/product.html')
def checkout(request):
    return render(request, 'checkout/checkout.html')
def home(request):
    return render(request, 'home/home.html')
def login(request):
    return render(request, 'login/login.html')
def cart(request):
    return render(request, 'cart/cart.html')
def index(request):
    posts = Post.objects.all()
 
    return render(request, 'blog/index.html',{'posts': posts})
