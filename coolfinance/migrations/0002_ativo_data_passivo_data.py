# Generated by Django 5.0.1 on 2024-04-05 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coolfinance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ativo',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='passivo',
            name='data',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
