# Generated by Django 4.2.5 on 2023-10-28 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admiss', '0004_studentregmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacherregmodel',
            old_name='phnno',
            new_name='phone',
        ),
    ]
