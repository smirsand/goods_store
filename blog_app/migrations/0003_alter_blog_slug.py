# Generated by Django 4.2.4 on 2023-09-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_blog_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(max_length=100, unique=True, verbose_name='slug'),
        ),
    ]
