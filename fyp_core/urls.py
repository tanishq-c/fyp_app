from django.contrib import admin
from django.urls import path

from ticket_resolution.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', login, name="home"),
    path(r'details/<int:id>', detailedView, name="details"),
]