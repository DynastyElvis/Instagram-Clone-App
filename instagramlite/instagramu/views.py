

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
