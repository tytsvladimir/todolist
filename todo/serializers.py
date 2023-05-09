from rest_framework import serializers
from .models import Category, Task

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]

class CategoryField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context['request'].user
        return Category.objects.filter(user=user)

class TaskSerializer(serializers.ModelSerializer):
    category = CategoryField(queryset=Category.objects.all())

    class Meta:
        model = Task
        fields = '__all__'
