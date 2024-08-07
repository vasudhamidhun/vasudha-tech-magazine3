# Generated by Django 4.2.5 on 2023-11-08 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admiss', '0013_apprejmodel_alter_applycoursemodel_certi_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='studentapprejmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uname', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('quali', models.CharField(max_length=20)),
                ('course', models.CharField(max_length=20)),
                ('spec', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('apprej', models.CharField(max_length=20)),
                ('reason', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='apprejmodel',
            name='details',
        ),
    ]
