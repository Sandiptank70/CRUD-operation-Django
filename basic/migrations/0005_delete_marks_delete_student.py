# Generated by Django 4.1.1 on 2022-09-25 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic', '0004_alter_student_course'),
    ]

    operations = [
        migrations.DeleteModel(
            name='marks',
        ),
        migrations.DeleteModel(
            name='student',
        ),
    ]
