from django.db import models
from tinymce.models import HTMLField
from django.contrib.auth.models import User
import datetime as dt

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    photo= models.ImageField(upload_to='profiles/',null=True)
    bio= HTMLField(max_length=240, null=True)


    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile


class Image(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to='image/',null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    caption = models.TextField(null=True)
    likes = models.PositiveIntegerField(default=0)
    posted = models.DateTimeField(auto_now_add=True)


    @classmethod
    def get_images(cls):
        Images = Image.objects.all()[::-1]
        return Images

    def __str__(self):
       return str(self.caption)

    
class Follow(models.Model):
    users=models.ManyToManyField(User,related_name='follow')
    current_user=models.ForeignKey(User,related_name='c_user',on_delete=models.SET_NULL,null=True)

    @classmethod
    def follow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.add(new)

    @classmethod
    def unfollow(cls,current_user,new):
        friends,created=cls.objects.get_or_create(current_user=current_user)
        friends.users.remove(new)


class Comment(models.Model):
    poster = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='comments',null=True)
    comment = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.comment

    def save_comment(self):
        self.save()

    @classmethod
    def get_comment(cls):
        comment = Comment.objects.all()[::-1]
        return comment


