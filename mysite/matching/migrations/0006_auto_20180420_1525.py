# Generated by Django 2.0.4 on 2018-04-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matching', '0005_delete_importfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='word',
            name='emotionty',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7')], default=0),
        ),
    ]
