# Generated by Django 3.2 on 2021-04-14 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_activity',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last activity time'),
        ),
    ]
