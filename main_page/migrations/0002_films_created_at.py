# Generated by Django 4.2.16 on 2024-11-07 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
