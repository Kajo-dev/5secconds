from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,get_user_model
from .models import User
from django.contrib.auth.decorators import login_required

from .tokens import account_activation_token
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login_page')
    else:
        pass #link nieprawidlowy

    return redirect('home_page')

def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("activate_account.html", {
        'user': user.first_name,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()



def register_page(request):
    error_list=[]
    if request.method == 'POST':
        email = request.POST['email']
        first_name = request.POST['first_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            error_list.append('Hasła nie są takie same')
        
        newUser = User.objects.create_user(email=email,first_name=first_name,password=password1)
        newUser.save()
        activateEmail(request,newUser,email)

        data_front = {
            'first_name':first_name,
            'email':email
        }

        return render(request,'confirmation_email.html',data_front)

        
    data_front = {
        'error_list':error_list,
    }
    return render(request,'register.html',data_front)

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