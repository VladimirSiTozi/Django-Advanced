from rest_framework import serializers

from toDoApp.accounts.serializers import UserSerializer
from toDoApp.todos.models import Category, Todo


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id']


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id']


class TodoReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    assignees = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['id', 'category', 'assignees']
