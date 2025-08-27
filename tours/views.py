from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request):
    """test_0 docstring"""
    return render(request, 'tours/index.html')


def departure_view(request, departure):
    """test_1 docstring"""
    return render(request, 'tours/departure.html')


def tour_view(request, tour_id):
    """test_2 docstring"""
    return render(request, 'tours/tour.html')


def custom_handler404(request, exception):
    """test_3 docstring"""
    return HttpResponseNotFound('Ошибка: 404')


def custom_handler500(exception):
    """test_4 docstring"""
    return HttpResponseServerError('Ошибка: 500')
