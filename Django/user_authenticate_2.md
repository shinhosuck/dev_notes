from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile
from .forms import ProfileUpdateForm



def create_user_view(request):
    form = UserCreationForm(request.POST or None, request.FILES or None)
    context = {
        'form': form
    }
    if form.is_valid():
        user_obj = form.save()
        pro_obj = Profile.objects.get(user=user_obj)
        pro_obj.username = user_obj.username
        pro_obj.save()
        context['form'] = UserCreationForm()
        messages.success(request, 'Successfully registered.')
        return redirect('users:login')
    return render(request, 'users/create_user.html', context)


def login_view(request):
    user = request.user
    if user.is_authenticated:
        messages.warning(request, 'You are logged in already.')
        return redirect('products:home')
    context = {
        "form": AuthenticationForm(request)
    }
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Successfully logged in.')
            return redirect("products:home")
        else:
            messages.error(request, 'Something went wrong.')
            context['form'] = form
    return render(request, 'users/login.html', context)


def logout_view(request):
    if not request.user.is_authenticated:
        messages.error(request, 'You are not logged in.')
        return redirect('users:login')
    else:
        if request.method == "POST":
            logout(request)
            messages.info(request, 'Successfully logged out.')
            return redirect('users:login')
        return render(request, 'users/logout.html', context=None)
    

def update_profile(request):
    user = request.user
    if not user.is_authenticated:
        messages.error(request, 'You must be logged in to update your profile.')
        return redirect('users:login')
    profile = Profile.objects.get(user=user)
    form = ProfileUpdateForm(request.POST or None, instance=profile)
    context = {
        'form': form
    }
    if form.is_valid():
        profile = form.save()
        user.first_name = profile.first_name
        user.last_name = profile.last_name
        user.save()
        messages.success(request, 'Profile successfully updated.')
        return redirect('products:home')
    else:
        context['form'] = form
    return render(request, 'users/update_profile.html', context)
