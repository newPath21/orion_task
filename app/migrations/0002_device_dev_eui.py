# Generated by Django 3.1.3 on 2022-07-27 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='dev_eui',
            field=models.CharField(default='E544334343', max_length=50, unique=True, verbose_name='идентификатор по устройству'),
        ),
    ]
