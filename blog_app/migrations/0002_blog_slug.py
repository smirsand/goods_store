# Generated by Django 4.2.4 on 2023-09-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='default-slug', max_length=100, verbose_name='slug'),
        ),
    ]