# Generated by Django 2.2.13 on 2022-11-20 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0014_auto_20221117_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='line',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='lineattribute',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]