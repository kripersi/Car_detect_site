from django.shortcuts import render, redirect, get_object_or_404
from add_car.models import Car


def search_car(request):
    query = request.GET.get('q', '').strip()

    if not query:
        return redirect('home')

    try:
        car = Car.objects.get(number_plate__iexact=query)
        return redirect('car_detail', pk=car.pk)
    except Car.DoesNotExist:
        return render(request, 'get_car/search_results.html', {'query': query, 'not_found': True})


def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'get_car/car_detail.html', {'car': car})
