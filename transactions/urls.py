from django.urls import path
from . import views

urlpatterns = [
    path('', views.money_transfer, name='money_transfer'),
    path('money_request/', views.money_request, name='money_request'),
    path('message/', views.message, name='message')
]
