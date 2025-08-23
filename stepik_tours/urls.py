from django.contrib import admin
from django.urls import path
import tours.views as tours_views
from tours.views import custom_handler404, custom_handler500

handler500 = custom_handler500
handler404 = custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', tours_views.main_view, name='main_view'),
    path('departure/<str:departure>', tours_views.departure_view, name='departure_view'),
    path('tour/<int:tour_id>', tours_views.tour_view, name='tour_view'),
]
