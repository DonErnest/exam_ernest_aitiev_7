# Generated by Django 2.2 on 2019-10-19 06:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='poll',
            name='updated_at',
        ),
    ]
