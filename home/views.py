from django.http import HttpResponse
from django.shortcuts import render, redirect, loader
from posts.models import Post
from home.models import SignUpForm, Profile
from django.contrib.auth import login, authenticate, logout
from django.core.mail import send_mail, EmailMultiAlternatives
from django.contrib import messages
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def redirecthome(request):
    post = Post.objects.get(pk=1)
    profileroot = Profile.objects.get(user_id=1)
    args = {'post':post, 'profileroot':profileroot}
    return render(request,  'home/home.html',args)

def loginuser(request):
    logout(request)
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if user.is_superuser:
                    return redirect('/admin')
                else:
                    return redirect('/cabinet')
    return render(request,'home/home.html')

def registrationuser(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password')

            user = User.objects.get(username=username)
            person_create = Profile(user_id=user.id)
            # person_create.save()
            user = authenticate(username=username, password=raw_password)
            messages.success(request,"Check Your Email")
            subject, from_email, to = 'Confirm account', 'dzurabyan@yandex.ru', email
            text_content = 'Confirm pleas your account.'
            html_content = '<p>Click  this link <a href=http://127.0.0.1:8000/confirm/'+username+'>Confirm</a> and activate your account.</p>'
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
    else:
        form = SignUpForm()
    return render(request,'home/home.html')
def cabinet(request):
    post = Post.objects.get(pk=1)
    profile =Profile.objects.get(user_id=request.user.id)
    profileroot = Profile.objects.get(user_id=1)

    args = {'post':post, 'profile':profile, 'profileroot':profileroot}
    if request.user.is_authenticated:
        return render(request, 'home/cabinet.html',args)
    else:
        return redirect('/')

def confirmuser(request, user):
    userobj = User.objects.get(username=user)
    userobj.is_staff=1
    userobj.save()
    login(request, userobj)

    return redirect('/cabinet')
