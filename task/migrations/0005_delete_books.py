# Generated by Django 4.2.5 on 2023-10-04 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_books'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]