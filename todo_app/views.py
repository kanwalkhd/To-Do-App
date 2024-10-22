from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

# Create your views here.
class ToDos(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):

        queryset = ToDo.objects.all()
        serialized = ToDoSerializer(queryset, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serializer = ToDoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request):
        try:
            todo = ToDo.objects.get(pk=request.data.get('id'))  # Get the existing object by primary key (or any identifier)
        except ToDo.DoesNotExist:
            return Response({"error": "To-Do not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ToDoSerializer(todo, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        pk = request.data.get('id')
        try:
            todo_object = ToDo.objects.get(pk=pk)
            todo_object.delete()
            return Response({'message': "todo deleted successfully"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UsersView(APIView):

    def get(self, request):
        queryset = User.objects.all()
        serialized = UserSerializer(queryset, many=True)
        return Response(serialized.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.create_user(serializer.data)
            Token.objects.create(user=user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)