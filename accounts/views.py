from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('website:index')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data['username']
                messages.success(request, 'Account was created for ' + user )
                return redirect('login')
        context = {'form':form}
        return render(request,'accounts/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('website:index')
    else:
        if request.method == 'POST':
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('website:index')
            else:
                messages.info(request,'Username Or password is incorrect')
                return render(request,'accounts/login.html') 
        context = {}
        return render(request,'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')