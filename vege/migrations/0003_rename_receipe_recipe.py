# Generated by Django 4.2.7 on 2023-11-24 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0002_rename_receipe_description_receipe_recipe_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Receipe',
            new_name='Recipe',
        ),
    ]