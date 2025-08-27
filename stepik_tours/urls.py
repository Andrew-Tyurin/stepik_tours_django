from django.contrib import admin
from django.urls import path, include
from tours.views import custom_handler404, custom_handler500

handler500 = custom_handler500
handler404 = custom_handler404

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tours.urls')),
]
