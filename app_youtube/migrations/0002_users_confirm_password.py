# Generated by Django 3.0.5 on 2020-04-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_youtube', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='confirm_password',
            field=models.CharField(default='', max_length=255),
        ),
    ]