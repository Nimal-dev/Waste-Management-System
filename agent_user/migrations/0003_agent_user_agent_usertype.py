# Generated by Django 4.2.7 on 2023-11-28 06:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agent_user', '0002_alter_agent_agent_img_alter_agent_licenses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agent',
            name='usertype',
            field=models.CharField(default='agent', max_length=10),
        ),
    ]