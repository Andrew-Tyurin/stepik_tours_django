from random import sample
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404
from . import data


def key_error(collection, key):
    try:
        collection_key = collection[key]
    except KeyError:
        raise Http404
    return collection_key


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


def departure_view(request, departure_url):
    city = key_error(data.departures, departure_url)
    tours_from_city = {}
    for key, value in data.tours.items():
        if departure_url == value['departure']:
            tours_from_city.setdefault(key, value)
    price_list = [tours_from_city[key]['price'] for key in tours_from_city]
    count_night = [tours_from_city[key]['nights'] for key in tours_from_city]

    return render(
        request,
        'tours/departure.html',
        {
            'tours_from_city': tours_from_city,
            'city': city,
            'count_tours': len(tours_from_city),
            'min_price': min(price_list),
            'max_price': max(price_list),
            'min_night': min(count_night),
            'max_night': max(count_night),
        }
    )


def tour_view(request, tour_id):
    """
    т.к URLs который отправляет сюда запрос, ожидает int,
    числа могут не совпадать с ключом. Проверим числа в
    функции key_error, чтобы избежать ошибки ServerError.
    И вызывать 'raise Http404'
    """
    tour = key_error(data.tours, tour_id)
    city = data.departures[tour['departure']]
    stars = range(int(tour['stars']))
    return render(
        request,
        'tours/tour.html',
        {'tour': tour, 'city': city, 'stars': stars}
    )


def custom_handler404(request, exception):
    return HttpResponseNotFound('Ошибка: 404')


def custom_handler500(exception):
    return HttpResponseServerError('Ошибка: 500')
