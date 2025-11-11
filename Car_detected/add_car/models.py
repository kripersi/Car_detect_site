from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

import os
from datetime import datetime

User = get_user_model()


def car_photo_upload_to(instance, filename):
    base, ext = os.path.splitext(filename)
    username = instance.car.added_by.username if instance.car and instance.car.added_by else "anon"
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    new_filename = f"{timestamp}_{username}{ext}"
    return f"add_car/{new_filename}"


class Car(models.Model):
    number_plate = models.CharField("Номер машины", max_length=20)
    owner = models.CharField("Владелец", max_length=100)
    previous_owners = models.TextField("Прошлые владельцы", max_length=250, blank=True, null=True)
    description = models.TextField("Описание машины", max_length=1000, blank=True, null=True)
    region = models.CharField("Страна", max_length=100, blank=True, null=True)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Кто добавил")
    added_at = models.DateTimeField("Дата добавления", default=timezone.now)

    def __str__(self):
        return f"{self.number_plate} ({self.owner})"


class CarPhoto(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='photos')
    image = models.ImageField("Фотография", upload_to=car_photo_upload_to)
    is_number_plate = models.BooleanField("На фото с номерным знаком", default=False)
