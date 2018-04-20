# Generated by Django 2.0.4 on 2018-04-19 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='diary_id',
        ),
        migrations.RemoveField(
            model_name='pairing',
            name='pair_id',
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(0, '0')], default=0),
        ),
    ]