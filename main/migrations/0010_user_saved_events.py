# Generated by Django 2.2.2 on 2019-06-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20190620_2130'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='saved_events',
            field=models.ManyToManyField(blank=True, to='main.Event'),
        ),
    ]
