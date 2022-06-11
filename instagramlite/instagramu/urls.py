from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.homepage, name='homepage'),
    url('like/(?P<operation>.+)/(?P<pk>\d+)',views.like, name='like'),
    url('profile/(\d+)', views.user_profile, name='profile'),
    url('new/profile', views.add_user_profile, name='add_profile'),
    url('search/', views.search_results, name='search_results'),
    url('comment/(?P<pk>\d+)',views.user_comments,name='comment'),
    url('follow/(?P<operation>.+)/(?P<id>\d+)',views.follow,name='follow'),
    url('upload/', views.upload_image, name='upload_image'),
    url('all/(?P<pk>\d+)', views.images, name='images'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)