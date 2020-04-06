# Generated by Django 3.0.3 on 2020-04-06 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_help', '0005_helprequest_times'),
    ]

    operations = [
        migrations.AlterField(
            model_name='helprequest',
            name='times',
            field=models.IntegerField(choices=[(5, '5 Minutes'), (10, '10 Minutes'), (15, '15 Minutes'), (30, '30 Minutes'), (60, '1 Hour')], default=5, max_length=6),
        ),
    ]
