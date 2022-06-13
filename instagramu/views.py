
from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
@login_required
def homepage(request):
    Images = Image.get_images()
    comments = Comment.get_comment()
    profile = Profile.get_profile()
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.save()
        return redirect('homepage')

    else:
        form = CommentForm()

    return render(request,"insta/homepage.html",{"Images":Images, "comments":comments,"form": form,"profile":profile})

@login_required
def user_profile(request,profile_id):
    try:
     profile = Profile.objects.get(pk=profile_id)

    except Profile.DoesNotExist:
      profile = None
    Images = Image.objects.filter(profile_id=profile).all()

    return render(request,"profile/profile.html",{"profile":profile,"Images":Images})


@login_required
def add_user_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('homepage')

    else:
        form = NewProfileForm()
    return render(request, 'profile/new_user_profile.html', {"form": form})


@login_required
def search_results(request):
    current_user = request.user
    profile = Profile.get_profile()
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_name = Profile.find_profile(search_term)
        message = search_term

        return render(request,'insta/search.html',{"message":message,"profiles":profile,"user":current_user,"username":searched_name})
    else:
        message = "You haven't searched for any username"
        return render(request,'insta/search.html',{"message":message})


@login_required
def user_comments(request,pk):
    image = get_object_or_404(Image, pk=pk)
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.image = image
            comment.poster = current_user
            comment.save()
            return redirect('homepage')
    else:
        form = CommentForm()
        return render(request,{"user":current_user,"comment_form":form})

def follow(request,operation,id):
    current_user=User.objects.get(id=id)
    if operation=='follow':
        Follow.follow(request.user,current_user)
        return redirect('homepage')
    elif operation=='unfollow':
        Follow.unfollow(request.user,current_user)
        return redirect('homepage')
        
def like(request,operation,pk):
    image = get_object_or_404(Image,pk=pk)
    if operation == 'like':
        image.likes += 1
        image.save()
    elif operation =='unlike':
        image.likes -= 1
        image.save()
    return redirect('homepage')

@login_required  
def upload_image(request):
    current_user = request.user
    profiles = Profile.get_profile()
    for profile in profiles:
        if profile.user.id == current_user.id:
            if request.method == 'POST':
                form = UploadForm(request.POST,request.FILES)
                if form.is_valid():
                    upload = form.save(commit=False)
                    upload.posted_by = current_user
                    upload.profile = profile
                    upload.save()
                    return redirect('homepage')
            else:
                form = UploadForm()
            return render(request,'insta/upload.html',{"user":current_user,"form":form})

def login_user(request):
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

     return render(request,'registration/login.html')

def register_user(request):
    if request.method == 'POST':
         form = UserRegisterForm(request.POST)
         if form.is_valid():
             form.save()
             username = form.cleaned_data['username']
             password = form.cleaned_data['password1']
             email = form.cleaned_data['email']
            #  send_welcome_email(username,email) 

             user = authenticate(username=username, password=password)
             login(request,user)

             messages.success(request,f'Hello {username}, Your account was Successfully Created.You will receive our email shortly.Thank You!!!')
             return redirect('add_profile')
    else:
         form = UserRegisterForm()
    return render (request,'registration/register.html',{'form':form})

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

@login_required
def images(request, pk):
    profile = Profile.objects.get(pk=pk)
    Images = Image.objects.all().filter(name=pk)

    return render(request, 'insta/images.html',{"profile": profile, 'Images': Images} )