from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from .models import User, Expense
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')

def log_in(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        try:
            user = get_user_model().objects.get(email=email)
        except:
            return render(request, 'login.html', {'message':'Please register!'})        
        if(user.password == password):
        # check if user exists
            if user is not None:
                login(request, user)
                request.session['username']=user.username
                return redirect('home')
            else:
                return redirect('login')
        else:
            return render(request, 'login.html', {'message':'Wrong Password!'})
    else:
        return render(request, 'login.html')


def log_out(request):
    logout(request)
    return redirect('login')
