# Generated by Django 3.1.1 on 2023-09-17 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_activity_club_studentmembership'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentmembership',
            name='club',
        ),
        migrations.RemoveField(
            model_name='studentmembership',
            name='student',
        ),
        migrations.DeleteModel(
            name='Activity',
        ),
        migrations.DeleteModel(
            name='Club',
        ),
        migrations.DeleteModel(
            name='StudentMembership',
        ),
    ]
