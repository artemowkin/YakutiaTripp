# Generated by Django 3.1.7 on 2021-03-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20210307_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
