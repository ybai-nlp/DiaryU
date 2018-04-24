# Generated by Django 2.0.4 on 2018-04-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0008_auto_20180420_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='title',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='sex',
            field=models.IntegerField(choices=[(0, '0'), (1, '1')], default=0, null=True),
        ),
    ]