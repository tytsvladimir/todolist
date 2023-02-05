from rest_framework import serializers
from .models import Todo


class TodoSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()
    category_id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    date_created = serializers.DateTimeField(read_only=True)
    date_expiration = serializers.DateTimeField()
    date_completed = serializers.DateTimeField(read_only=True)
    is_important = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Todo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id', instance.user_id)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.date_expiration = validated_data.get('date_expiration', instance.date_expiration)
        instance.date_completed = validated_data.get('date_completed', instance.date_completed)
        instance.is_important = validated_data.get('is_important', instance.is_important)
        instance.save()
        return instance
