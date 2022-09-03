# Generated by Django 4.0.2 on 2022-08-30 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('pronoun', models.CharField(choices=[('S', 'She/her/hers'), ('H', 'He/him/his'), ('T', 'They/them/theirs'), ('O', 'Other')], max_length=10)),
                ('photo', models.URLField()),
                ('bio', models.CharField(max_length=1000)),
                ('date_created', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]