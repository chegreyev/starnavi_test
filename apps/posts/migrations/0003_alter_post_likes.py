# Generated by Django 3.2 on 2021-04-14 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, to='posts.Like'),
        ),
    ]
