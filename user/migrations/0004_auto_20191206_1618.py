# Generated by Django 2.2.7 on 2019-12-06 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_profile_designation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='designation',
        ),
    ]