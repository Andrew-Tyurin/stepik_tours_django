from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('departure/<str:departure_url>', views.departure_view, name='departure_view'),
    path('tour/<int:tour_id>', views.tour_view, name='tour_view'),
]
