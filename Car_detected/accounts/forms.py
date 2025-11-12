from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from django import forms
from add_car.models import Car


class RegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'first_name', 'last_name', 'bio', 'password1', 'password2']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number_plate', 'owner', 'previous_owners', 'description', 'region']
