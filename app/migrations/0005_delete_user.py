# Generated by Django 4.0.4 on 2022-06-10 10:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]