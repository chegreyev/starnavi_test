# Generated by Django 3.2 on 2021-04-14 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_alter_post_likes'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={'verbose_name': 'Лайк/Дизлайк', 'verbose_name_plural': 'Лайки/Дизлайки'},
        ),
    ]
