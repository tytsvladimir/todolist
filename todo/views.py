from rest_framework import generics, viewsets

from .models import Todo, Category
from .serializers import TodoSerializer


class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

# class TodoAPIListView(generics.ListCreateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
#
# class TodoAPIUpdateView(generics.UpdateAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer
#
# class TodoAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer