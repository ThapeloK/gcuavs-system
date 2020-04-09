from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

@login_required(login_url='login')
def loginPage(request):
    if request.method =='POST':
       username = request.POST.get('username')
       password = request.POST.get('password')

       user = authenticate(request, username=username, password=password)

       if user is not None:
           login(request, user)
           return redirect('index')
       else:
           messages.info(request, 'Username OR password is incorrect')
           
    context = {}
    return render (request, 'users/login.html', context)

def profile(request):
    return render(request, 'users/profile.html')