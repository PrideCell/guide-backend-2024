# Generated by Django 4.2 on 2024-01-22 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0015_alter_team_student_1_marks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='student_1_marks',
        ),
        migrations.RemoveField(
            model_name='team',
            name='student_2_marks',
        ),
    ]
