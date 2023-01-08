from django.core.management.base import BaseCommand
from todolist.models import TodoItem
class Command(BaseCommand):
    help = 'Delete completed items.'

    def handle(self, *args, **kwargs):
        completed_items=TodoItem.objects.filter(is_completed=1)
        completed_items_len=len(completed_items)
        completed_items.delete()
        self.stdout.write(f"{completed_items_len} was deleted.")