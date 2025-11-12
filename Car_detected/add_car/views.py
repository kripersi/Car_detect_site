from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CarForm, CarPhotoUploadForm
from .models import Car, CarPhoto
from django.contrib import messages


@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        photo_form = CarPhotoUploadForm(request.POST, request.FILES)
        if form.is_valid() and photo_form.is_valid():
            # сохраняем машину
            car = form.save(commit=False)
            car.added_by = request.user
            car.save()

            # проверка, есть ли фото с номерным знаком
            has_number_plate_photo = False

            # собираем все фотографии
            for i in range(1, 6):
                photo_field = 'image{}'.format(i)
                if photo_form.cleaned_data.get(photo_field):
                    is_num_plate = photo_form.cleaned_data.get(f'is_number_plate{i}', False)
                    if is_num_plate:
                        has_number_plate_photo = True
                    photo = CarPhoto(
                        car=car,
                        image=photo_form.cleaned_data.get(photo_field),
                        is_number_plate=is_num_plate
                    )
                    photo.save()

            if not has_number_plate_photo:
                messages.error(request, "Обязательно должна быть фотография с номерным знаком.")
                # Удаляем созданную машину, если фото с номерным знаком отсутствует
                car.delete()
                return render(request, 'add_car/add_car.html', {'form': form, 'photo_form': photo_form})

            # Успешно добавлено
            messages.success(request, "Машина успешно добавлена")
            return redirect('home')
    else:
        form = CarForm()
        photo_form = CarPhotoUploadForm()

    return render(request, 'add_car/add_car.html', {'form': form, 'photo_form': photo_form})
