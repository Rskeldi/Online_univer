# Generated by Django 3.1.3 on 2020-11-15 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Task', '0003_auto_20201115_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='mark',
            field=models.IntegerField(default=0),
        ),
    ]
