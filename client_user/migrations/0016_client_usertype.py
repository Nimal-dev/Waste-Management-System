# Generated by Django 4.2.7 on 2023-11-28 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client_user', '0015_client_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='usertype',
            field=models.CharField(default='client', max_length=10),
        ),
    ]
