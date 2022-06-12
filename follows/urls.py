from . import views
from django.urls import path

urlpatterns=[
    path('accounts/login/',views.login_users,name='login'),
    path('logout/',views.logout_users,name='logout'),
    path('register/',views.register,name='register'),
 
]