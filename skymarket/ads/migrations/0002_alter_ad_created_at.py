# Generated by Django 3.2.6 on 2023-01-05 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
