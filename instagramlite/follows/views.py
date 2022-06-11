from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# Create your views here.
def register(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data.get('username')
             messages.success(request,f'Account for {username},  was successfully created!! Feel Free to Login.')
             return redirect('homepage')
    else:
         form = UserRegisterForm()
    return render (request,'users/register.html',{'form':form})

def login_users(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
         login(request, user)
         return redirect('homepage')
        
        else:
            messages.success(request,('Invalid information'))
            return redirect('login')
         
    else:

     return render(request,'users/login.html')


@login_required
def logout_users(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

