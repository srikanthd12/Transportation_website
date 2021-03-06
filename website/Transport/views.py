from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.db.models import Q
# Create your views here.
from Transport.forms import *

def index(request):
     if not request.user.is_authenticated():
           return render(request, 'Transport/login.html')
     else:
           return render(request,'Transport/index.html') 	   
 

def Booking(request):
    form = BookingForm()
    context = {
    "form": form,
    }
    return render(request,"Transport/Booking.html",context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return render(request, 'Transport/index.html')
            else:
                return render(request, 'Transport/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'Transport/login.html', {'error_message': 'Invalid login'})
    return render(request, 'Transport/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'Transport/login.html', context)


def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
             
                return render(request, 'Transport/index.html')
    context = {
        "form": form,
    }
    return render(request, 'Transport/register.html', context)


