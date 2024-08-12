from django.shortcuts import render

# Create your views here.
def App(request):
    return render(request, 'App/App.html')
def home(request):
    return render(request, 'home/home.html')
def login(request):
    return render(request, 'login/login.html')