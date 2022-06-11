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


