from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.shortcuts import render, get_object_or_404
from .models import CustomUser
from add_car.models import Car
from .forms import CarForm


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
    cars = Car.objects.filter(added_by=request.user)
    return render(request, 'accounts/account.html', {'cars': cars})


@login_required
def edit_car(request, pk):
    car = get_object_or_404(Car, id=pk, added_by=request.user)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('account')
    else:
        form = CarForm(instance=car)

    return render(request, 'accounts/edit_car.html', {'form': form, 'car': car})


@login_required
def delete_car(request, pk):
    car = get_object_or_404(Car, pk=pk, added_by=request.user)
    car.delete()
    return redirect('account')


def user_logout(request):
    logout(request)
    return redirect('home')


def public_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    return render(request, 'accounts/public_profile.html', {'profile_user': user})

