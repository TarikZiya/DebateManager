# Generated by Django 5.0.3 on 2024-05-29 11:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM', '0008_remove_blog_category_blog_categories'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='categories',
        ),
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='DM.category'),
        ),
    ]
