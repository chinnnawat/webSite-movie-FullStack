# Generated by Django 4.2.4 on 2023-09-28 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webBlogs', '0004_remove_webblogs_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='webblogs',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
