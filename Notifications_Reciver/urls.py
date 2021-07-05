from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Notifications_Reciver-home'),
    path('about/', views.about, name='Notifications_Reciver-about'),
]
