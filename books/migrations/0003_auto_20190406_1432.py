# Generated by Django 2.1.4 on 2019-04-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20190406_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='about',
            field=models.CharField(default='Description not available.', max_length=10000),
        ),
        migrations.AddField(
            model_name='book',
            name='cover',
            field=models.CharField(default='Image not available.', max_length=1000),
        ),
    ]
