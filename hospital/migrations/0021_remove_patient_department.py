# Generated by Django 3.0.5 on 2022-11-29 02:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0020_auto_20221129_0711'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='department',
        ),
    ]
