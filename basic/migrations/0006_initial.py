# Generated by Django 4.1.1 on 2022-09-25 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('basic', '0005_delete_marks_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdid', models.IntegerField(max_length=120, unique=True)),
                ('Fname', models.CharField(max_length=20)),
                ('Lname', models.CharField(max_length=20)),
                ('Mname', models.CharField(max_length=20)),
                ('course', models.CharField(choices=[('MCA', 'MCA'), ('II', 'IT'), ('COMPUTER', 'COMPUTER')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='marks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmark', models.IntegerField()),
                ('cppmark', models.IntegerField()),
                ('pymark', models.IntegerField()),
                ('stdid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='basic.student')),
            ],
        ),
    ]
