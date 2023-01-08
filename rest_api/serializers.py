from todolist.models import TodoItem
from rest_framework import serializers

class TodoItemSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= TodoItem
        fields = ["title","is_completed"]
