from django.urls import path
from .views import *
urlpatterns = [
    path('', ToDo.as_view())
]