from django.shortcuts import render,redirect
from django.urls import reverse
from django.views import View
from todolist.models import TodoItem
from todolist.forms import TodoItemForm
from datetime import datetime

class TodoListView(View):
    

    def get(request):
        # completed_item_form=CompletedItemForm()
        
        todo_item=TodoItem.objects.all()
        # print(todo_item[11].title)
        # print(todo_item[11].is_completed)
        todo_items_list=todo_item.order_by("-created_at")
        if(request.POST):
            todoItem_form=TodoItemForm(request.POST)
            if(todoItem_form.is_valid()):
                todoItem_form.save()
                return redirect(reverse('get_todo_list'))
        else:
            todoItem_form=TodoItemForm()
        context={
            'todo_items_list': todo_items_list,
            'todoItem_form':todoItem_form
        }
        return render(request, 'todolist.html', context)

    def update_completed_item(request,id):
        if(request.POST):
            todo_item=TodoItem.objects.get(id=id)
            print(todo_item)
            todo_item.is_completed=True
            todo_item.save()
            return redirect(reverse('get_todo_list'))
        #     item_from_request=request.POST["is_checked12"]
        #     item_from_db=TodoItem.objects.get(title=item_from_request)
        #     print(item_from_db)
        #     # print(completed_item_form)
        #     # if(completed_item_form.is_valid()):
        #     #     item=completed_item_form.cleaned_data['is_checked']
        #     #     print(item)
        
            
            # completed_item_form=CompletedItemForm()
        return redirect(reverse('get_todo_list'))

        
    def delete_item(request,id):
        
        todo_item=TodoItem.objects.get(id=id)
        print(todo_item)
        
        todo_item.delete()
        return redirect(reverse('get_todo_list'))


    
