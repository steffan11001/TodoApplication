from django import forms 
from todolist.models import TodoItem
from django.utils.translation import gettext_lazy as _

class TodoItemForm(forms.ModelForm):
    class Meta:
        model=TodoItem
        fields=['title']
        labels={
            'title':_('Enter to do item:')
        }
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control todo-list-input',
                                            'placeholder':'What do you need to do today?'}),
        }
        error_messages={
            'title':{
                'required':_('You cannot move forward without todoItem')
            }
        }
class CompletedItemForm(forms.Form):
    is_checked=forms.BooleanField()