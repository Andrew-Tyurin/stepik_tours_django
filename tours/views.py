from random import sample
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError, Http404, HttpRequest, HttpResponse
from . import data


def key_error(collection: dict, key: str | int) -> str | dict:
    """
    Функция проверяет чтобы urls/запрос пользователя
    был ключом словаря из moc-data и возвращает значение ключа,
    иначе вызываем исключение not found(error404).
    """
    try:
        collection_key = collection[key]
    except KeyError:
        raise Http404
    return collection_key


def data_filter(collection: dict, key: str) -> list:
    """
    Функция возвращает список значений конкретного ключа
    """
    return [collection[i][key] for i in collection]


def main_view(request: HttpRequest) -> HttpResponse:
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


def departure_view(request: HttpRequest, departure_url: str) -> HttpResponse:
    city = key_error(data.departures, departure_url)
    tours_from_city = {}
    for key, value in data.tours.items():
        if departure_url == value['departure']:
            tours_from_city.setdefault(key, value)
    price_list = data_filter(tours_from_city, 'price')
    count_night = data_filter(tours_from_city, 'nights')
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


def tour_view(request: HttpRequest, tour_id: int) -> HttpResponse:
    tour = key_error(data.tours, tour_id)
    city = data.departures[tour['departure']]
    stars = range(int(tour['stars']))
    return render(
        request,
        'tours/tour.html',
        {'tour': tour, 'city': city, 'stars': stars}
    )


def custom_handler404(request: HttpRequest, exception: Http404) -> HttpResponse:
    return HttpResponseNotFound('Ошибка: 404 - страница не найдена')


def custom_handler500(exception: HttpRequest) -> HttpResponse:
    return HttpResponseServerError('Ошибка: 500 - проблема на сервере')
