# create serializers for todo
# Path: core/todo/serializers.py
from rest_framework import serializers
from core.todo.models import Todo


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        read_only_fields = ['created', 'updated']
