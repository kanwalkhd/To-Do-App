from django.urls import path, include
from .views import *


urlpatterns = [
    path('todo', ToDos.as_view()),
    path('user', UsersView.as_view())
]