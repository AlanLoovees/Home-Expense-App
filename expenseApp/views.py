from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, logout
from django.contrib.auth.decorators import login_required
from .models import User, Expense
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
import datetime

# Create your views here.

@login_required(login_url='login')
def home(request):
    expense = Expense.objects.all().filter(entryType='expense')
    income = Expense.objects.all().filter(entryType='income')
    expenseTotal = 0
    incomeTotal = 0

    if(expense):
        for expenses in expense.iterator():
            expenseTotal = expenseTotal + expenses.amount

    if(income):
        for incomes in income.iterator():
            incomeTotal = incomeTotal + incomes.amount
    
    total = incomeTotal - expenseTotal
    return render(request, 'home.html', {'expenseTotal': expenseTotal, 'incomeTotal':incomeTotal, 'total': total})

@login_required(login_url='login')
def logs(request):
    return render(request, 'log.html')

@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        date = request.POST['date']
        entryType = request.POST['expenseType']
        amount = request.POST['amount']
        username = request.session['username']

        newEntry = Expense(username=username, date=date, entryType=entryType, amount=amount)
        newEntry.save()

    return redirect('home')

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
