# Generated by Django 5.0.6 on 2024-07-13 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
