from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def homeView(request):
    return render(request, 'home.html')


def loginView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=name, password=password)
        print(name, password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('username and password are incorrect')

    return render(request, 'login_page.html')


def sighupView(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')
        password_2 = request.POST.get('password2')
        if password != password_2:
            return HttpResponse('password and conformation password are not same.')
        else:
            my_user = User.objects.create_user(name, email, password)
            my_user.save()
            return redirect('login')
        # print(name, email, password, password_2)
    return render(request, 'signup.html')


def logoutView(request):
    logout(request)
    return redirect('login')
