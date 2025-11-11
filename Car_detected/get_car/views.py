from django.shortcuts import render, redirect, get_object_or_404
from add_car.models import Car


def search_car(request):
    query = request.GET.get('q', '').strip()
    if query:
        try:
            # ищем автомобиль по номеру (игнорирую регистр)
            car = Car.objects.get(number_plate__iexact=query)
            # Перенаправляем на страницу деталей автомобиля (предположим, с названием 'car_detail')
            return redirect('car_detail', pk=car.pk)
        except Car.DoesNotExist:
            # Не нашли — показываем сообщение
            return render(request, 'get_car/search_results.html', {'query': query, 'not_found': True})
    else:
        # ничего не ввели — просто показываем сообщение или страницу поиска
        return render(request, 'get_car/search_results.html', {'query': '', 'not_found': False})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'get_car/car_detail.html', {'car': car})

