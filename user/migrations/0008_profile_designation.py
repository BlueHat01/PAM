# Generated by Django 2.2.7 on 2019-12-06 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_remove_profile_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='designation',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]