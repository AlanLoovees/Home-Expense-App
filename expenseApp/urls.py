from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('login', views.log_in, name='login'),
    path('logs', views.logs, name='logs'),
    path('add', views.add, name='add'),
    path("log_out", views.log_out, name="log_out"),
]
