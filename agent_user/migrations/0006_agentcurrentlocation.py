# Generated by Django 4.2.7 on 2023-11-28 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent_user', '0005_agent_latitude_agent_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='AgentCurrentLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.TextField(null=True)),
                ('longitude', models.TextField(null=True)),
                ('agent', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='agent_user.agent')),
            ],
        ),
    ]