from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('speakers/', views.speakers, name='speakers'),
    path('schedule/', views.schedule, name='schedule'),
    path('register/', views.register, name='register'),
    path('payment/', views.payment, name='payment'),

]
