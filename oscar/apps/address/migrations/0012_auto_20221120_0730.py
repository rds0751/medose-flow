# Generated by Django 2.2.13 on 2022-11-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0011_alter_useraddress_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
