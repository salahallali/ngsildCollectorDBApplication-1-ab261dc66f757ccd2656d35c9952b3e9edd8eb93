from django.urls import path
from . import views

urlpatterns = [
    path('entities/', views.Request_entity.as_view(), name='request_manager-request_entity'),
    path('subscriptions/', views.Request_subscription.as_view(), name='request_manager-request_subscription')
]
