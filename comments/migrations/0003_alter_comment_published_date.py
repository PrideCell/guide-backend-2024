# Generated by Django 4.0.4 on 2023-03-19 12:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_alter_comment_guide_alter_comment_guide_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
