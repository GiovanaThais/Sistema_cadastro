# Generated by Django 4.0.1 on 2022-01-27 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plataforma', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cidade',
            name='nome',
            field=models.CharField(max_length=30, verbose_name='nome'),
        ),
    ]
