# Generated by Django 5.0.6 on 2024-07-13 09:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0002_alter_postmodel_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='postmodel',
            options={'ordering': ('-date_created',)},
        ),
    ]
