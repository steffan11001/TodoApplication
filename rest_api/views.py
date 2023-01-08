from todolist.models import TodoItem
from rest_api.serializers import TodoItemSerializer
from django.http.response import JsonResponse

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers

# Create your views here.

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_todoYtems': '/',
        'Search by title': '/?title=title_name',
        'Add': '/create',
        'Update': '/update/title',
        'Delete': '/todoItem/title/delete'
    }
    return Response(api_urls)
@api_view(['POST'])
def add_todo_items(request):
    todoItem = TodoItemSerializer(data=request.data)
  
    # validating for already existing data
    if TodoItem.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')
  
    if todoItem.is_valid():
        todoItem.save()
        return Response(todoItem.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def view_todo_items(request):
    
    # checking for the parameters from the URL
    if request.query_params:
        todoItems = TodoItem.objects.filter(**request.query_param.dict())
    else:
        todoItems = TodoItem.objects.all()
  
    # if there is something in items else raise error
    if todoItems:
        data = TodoItemSerializer(todoItems,many=True)
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def update_todo_items(request, title):
    todoItems = TodoItem.objects.get(title=title)
    data = TodoItemSerializer(instance=todoItems, data=request.data)
  
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['DELETE'])
def delete_todo_items(request, title):
    todoItems = TodoItem.objects.get(title=title)
    print(f"delete this{todoItems}")
    todoItems.delete()
    return Response(status=status.HTTP_202_ACCEPTED)

    # return JsonResponse({'message': 'TodoItem was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


class TodoItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows todoItems to be viewed or edited.
    """
    queryset = TodoItem.objects.all().order_by('-created_at')
    serializer_class = TodoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

