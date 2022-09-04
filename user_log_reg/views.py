from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from .models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register_page(request):
    error_list=[]
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error_list.append('Hasła nie są takie same')
            
        try:
            newUser = User.objects.create_user(email=email,first_name=first_name,password=password1)
            newUser.save()
            return redirect('login_page')
        except:
            messages.error(request,'Error unsp')
        

    errory = {
        'lista':error_list
    }

    return render(request,'register.html',errory)


def login_page(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('home_page')
        else:
            return redirect('login_page')

    return render(request,'login.html',{})


@login_required(login_url='login_page')
def logout_page(request):
    logout(request)
    return render(request,'logout.html',{})