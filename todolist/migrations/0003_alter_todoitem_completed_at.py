# Generated by Django 3.2.5 on 2022-11-10 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0002_todoitem_completed_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='completed_at',
            field=models.DateTimeField(null=True),
        ),
    ]
