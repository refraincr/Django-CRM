from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    # return  render(request,'website/home.html',{})
    if request.method == "POST":
        username  = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials...")
            return redirect('home')
    else:
        return render(request,'website/home.html',{})


def logout_view(request):
    logout(request)
    messages.success(request, "You are now logged out...")
    return redirect('home')

def register_view(request):
    return render(request,'website/register.html',{})