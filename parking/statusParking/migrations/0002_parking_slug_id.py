# Generated by Django 3.2.3 on 2022-05-10 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('statusParking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='slug_id',
            field=models.SlugField(max_length=12, null=True),
        ),
    ]
