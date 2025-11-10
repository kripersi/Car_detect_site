from django import forms
from .models import Car, CarPhoto


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['number_plate', 'region', 'owner', 'previous_owners', 'description']


class CarPhotoUploadForm(forms.Form):
    image1 = forms.ImageField(label='Фотография 1 (обязательно с номерным знаком)')
    image2 = forms.ImageField(label='Фотография 2', required=False)
    image3 = forms.ImageField(label='Фотография 3', required=False)
    image4 = forms.ImageField(label='Фотография 4', required=False)
    image5 = forms.ImageField(label='Фотография 5', required=False)
    is_number_plate1 = forms.BooleanField(label='На фото с номерным знаком', required=False)

