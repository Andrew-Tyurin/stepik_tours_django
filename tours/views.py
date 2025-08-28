from random import sample
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from . import data


def main_view(request):
    subtitle = data.subtitle
    description = data.description
    tours_random = {}
    for key in sample(list(data.tours), 6):
        tours_random.setdefault(key, data.tours[key])
    return render(
        request,
        'tours/index.html',
        {'tours_random': tours_random, 'subtitle': subtitle, 'description': description}
    )


def departure_view(request, departure):
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    """
    т.к URLs который отправляет сюда запрос, ожидает int,
    числа могут не совпадать с ключами наших данных(если
    в эту функцию попадёт неправильное число, то будет
    исключение ServerError - это будет не корректно).
    Тогда мы вызываем not found, raise Http404
    """
    if tour_id in data.tours:
        tour = data.tours[tour_id]
        city = data.departures[tour['departure']]
        stars = range(int(tour['stars']))
        return render(
            request,
            'tours/tour.html',
            {'tour': tour, 'city': city, 'stars': stars}
        )
    raise Http404('Нету страницы с таким номером')


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка: 404')


def custom_handler500(exception):
    return HttpResponseServerError('Ошибка: 500')
