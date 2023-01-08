from django.urls import path

from todolist.views import TodoListView

urlpatterns = [
    path('', TodoListView.get, name="get_todo_list"),
    path('update_completed_item/<int:id>/', TodoListView.update_completed_item, name="update_completed_item"),
    path('delete_item/<int:id>/', TodoListView.delete_item, name="delete_item"),

    # path('add_todo_item/', TodoListView.add_item, name="add_todo_item")
]
