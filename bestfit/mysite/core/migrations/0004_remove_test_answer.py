# Generated by Django 2.2.7 on 2019-12-05 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20191205_1410'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='test',
            name='answer',
        ),
    ]
