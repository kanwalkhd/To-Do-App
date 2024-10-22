from django.shortcuts import render
from django.http import JsonResponse
from django.views import View


# Create your views here.
class ToDo(View):

    def get(self, request):
        return JsonResponse({'message': "get view of todolist"})
