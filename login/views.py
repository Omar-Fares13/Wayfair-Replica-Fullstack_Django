from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login/login.html')
def home(request):
    return render(request, 'home/home.html')