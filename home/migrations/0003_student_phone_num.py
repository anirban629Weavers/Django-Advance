# Generated by Django 4.2.7 on 2023-11-24 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='phone_num',
            field=models.CharField(default='1234567890', max_length=11),
        ),
    ]
