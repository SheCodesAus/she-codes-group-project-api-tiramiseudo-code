# Generated by Django 4.0.2 on 2022-09-03 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_rename_users_skill_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='user',
            field=models.ManyToManyField(related_name='skills', to='users.User'),
        ),
    ]
