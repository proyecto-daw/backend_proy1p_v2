# Generated by Django 2.2.2 on 2019-06-19 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190618_0012'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='blocked',
            field=models.BooleanField(default=False),
        ),
    ]
