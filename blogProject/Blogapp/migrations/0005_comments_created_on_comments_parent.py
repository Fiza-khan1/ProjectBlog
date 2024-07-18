# Generated by Django 5.0.6 on 2024-07-17 06:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0004_comments'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='created_on',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Blogapp.comments'),
        ),
    ]
