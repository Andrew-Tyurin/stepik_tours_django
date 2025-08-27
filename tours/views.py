from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError
from . import data


def main_view(request):
    """test_0 docstring"""
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    """test_1 docstring"""
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    if tour_id in data.tours:
        tour = data.tours[tour_id]
        city = data.departures[tour['departure']]
        stars = range(int(tour['stars']))
        return render(
            request,
            'tours/tour.html',
            {'tour': tour, 'city': city, 'stars': stars}
        )
    return custom_handler404(request, HttpResponseNotFound)


def custom_handler404(request, exception):
    """test_3 docstring"""
    return HttpResponseNotFound('Ошибка: 404')


def custom_handler500(exception):
    """test_4 docstring"""
    return HttpResponseServerError('Ошибка: 500')
