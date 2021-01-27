from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('home', views.home, name='home'),
    # path('start', views.start, name='start'),
    # path('quiz', views.quiz, name='quiz'),
    # path('result', views.result, name='result'),
    # path("thank_exam", views.thank_exam, name="thank_exam"),
    # path('login', views.log_in, name='login'),
    # path("log_out", views.log_out, name="log_out"),
    # path('admin', views.admin, name='admin'),
    # path('admin/answers', views.admin_answers, name='admin_answers'),
    # path("admin/log_out", views.log_out, name="log_out"),
    # path('register', views.register, name='register'),
]
