from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


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
    image = models.ImageField("Фотография", upload_to='add_car/')
    is_number_plate = models.BooleanField("На фото с номерным знаком", default=False)
