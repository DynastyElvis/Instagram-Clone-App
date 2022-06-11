from django.test import TestCase
from .models import *

# Create your tests here.

class ProfileTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'love life')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('cherry')
        self.assertTrue(len(profile) > 0)

class ImageTestClass(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')
        self.profile = Profile.objects.create(user = self.user,bio = 'love life')

        self.image = Image.objects.create(name = self.user,profile = self.profile,caption ='full vibe',likes = 0,posted='3/06/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.image,Image))

    def test_get_images(self):
        self.image.save()
        image = Image.get_images()
        self.assertTrue(len(image) == 1)

class CommentTestClass(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='cherry')

        self.comment= Comment.objects.create(poster= self.user, comment='new comment' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)

