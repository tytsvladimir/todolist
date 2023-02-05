from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo, Category
from .serializers import TodoSerializer


class TodoAPIView(APIView):
    def get(self, request):
        data = Todo.objects.all()
        return Response({'todos': TodoSerializer(data, many=True).data})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'todo_new': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method PUT not allowed'})
        try:
            instance = Todo.objects.get(pk=pk)
        except:
            return Response({'error': 'Objects does not exists'})

        serializer = TodoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'todo': serializer.data})

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if not pk:
            return Response({'error': 'Method DELETE not allowed'})
        try:
            instance = Todo.objects.get(pk=pk)
        except:
            return Response({'error': 'Object does not exists'})

        instance.delete()

        return Response({'todo': 'Delete todo ' + str(pk)})
