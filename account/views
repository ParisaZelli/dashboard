from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def login_view(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect(to='/')
       
        
    return render(request,'account/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect(to='/')


def sign_up(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='/')
        else:
            return HttpResponse('something is wrong')
    form=UserCreationForm()
    return render(request,'account/signup.html',{'form':form})
