import os
import cv2
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CarForm, CarPhotoUploadForm
from .models import Car, CarPhoto


def detect_number_plate(image_path):
    """
    Проверяет, есть ли на фото номерной знак (через Haar Cascade).
    Возвращает True, если найден.
    """
    cascade_path = os.path.join(settings.BASE_DIR, 'add_car', 'cascades', 'haarcascade_russian_plate_number.xml')

    if not os.path.exists(cascade_path):
        print("⚠️ Не найден файл каскада:", cascade_path)
        return False

    plate_cascade = cv2.CascadeClassifier(cascade_path)
    img = cv2.imread(image_path)

    if img is None:
        print("⚠️ Не удалось загрузить изображение:", image_path)
        return False

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=4,
        minSize=(25, 25)
    )

    return len(plates) > 0


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

            has_number_plate_photo = False

            # Проверяем первую фотографию на наличие номерного знака
            image1 = photo_form.cleaned_data.get('image1')
            if image1:
                temp_dir = os.path.join(settings.MEDIA_ROOT, 'temp')
                os.makedirs(temp_dir, exist_ok=True)

                temp_path = os.path.join(temp_dir, 'temp_image1.jpg')
                with open(temp_path, 'wb+') as f:
                    for chunk in image1.chunks():
                        f.write(chunk)

                if detect_number_plate(temp_path):
                    has_number_plate_photo = True
                    print("Найден номерной знак на фото 1")
                else:
                    print("Номерной знак не найден на фото 1")

                os.remove(temp_path)

            # --- Если номер не найден — ошибка ---
            if not has_number_plate_photo:
                messages.error(
                    request,
                    "⚠️ На первой фотографии не найден номерной знак. "
                    "Пожалуйста, загрузите фото, где номер чётко виден."
                )
                car.delete()  # удаляем временно созданную запись
                return render(request, 'add_car/add_car.html', {
                    'form': form,
                    'photo_form': photo_form
                })

            # Сохраняем все фотографии
            for i in range(1, 6):
                photo_field = f'image{i}'
                if photo_form.cleaned_data.get(photo_field):
                    photo = CarPhoto(
                        car=car,
                        image=photo_form.cleaned_data[photo_field],
                        is_number_plate=(i == 1 and has_number_plate_photo)
                    )
                    photo.save()

            messages.success(request, "Машина успешно добавлена")
            return redirect('home')

    else:
        form = CarForm()
        photo_form = CarPhotoUploadForm()

    return render(request, 'add_car/add_car.html', {'form': form, 'photo_form': photo_form})
