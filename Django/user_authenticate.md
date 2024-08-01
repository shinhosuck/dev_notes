from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import Http404



def home(request):
    print(request.session.get('attempt'))
    return render(request, 'users/home.html', {})


def register_view(request):
    form = RegisterForm(request.POST or None)
    context = {'form': form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        confirm_password = form.cleaned_data.get('confirm_password')
        email = form.cleaned_data.get('email')
        new_user = User.objects.create_user(username=username, email=email, password=password)
        print(new_user)
        return redirect('users:login')
    else:
        context = {'form':form, 'error':'Form is invalid'}
    return render(request, 'users/register.html', context)


def login_view(request):
    redirect_url = request.GET.get('next') # redirect url
    form = LoginForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if redirect_url:
                return redirect(redirect_url)
            return redirect('home')
        else:
            context = {'form': form, 'error': 'User does not exist'}

        attempt = request.session.get('attempt')
        if attempt == None:
            request.session['attempt'] = 1
        else:
            request.session['attempt'] = attempt + 1
        num_of_tries = request.session.get('attempt')
        
    return render(request, 'users/login.html', context)


@login_required
def logout_view(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        return redirect('home')
    return render(request, 'users/logout.html', {})
