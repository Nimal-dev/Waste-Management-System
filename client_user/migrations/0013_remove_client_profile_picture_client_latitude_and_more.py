# Generated by Django 4.2.7 on 2023-11-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_user', '0012_client_profile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='profile_picture',
        ),
        migrations.AddField(
            model_name='client',
            name='latitude',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='location',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.TextField(null=True),
        ),
    ]
