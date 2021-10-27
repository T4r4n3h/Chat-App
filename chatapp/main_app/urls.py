from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('chatapp/myhome', views.myhome, name='myhome'),
    path('index', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]
