# Generated by Django 3.2.16 on 2022-11-14 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communication', '0006_auto_20221107_1544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communicationeventtype',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='email',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
