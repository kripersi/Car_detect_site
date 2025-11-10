from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404
from .models import CustomUser


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def account(request):
    return render(request, 'accounts/account.html')


def user_logout(request):
    logout(request)
    return redirect('home')


def public_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'accounts/public_profile.html', {'profile_user': user})


