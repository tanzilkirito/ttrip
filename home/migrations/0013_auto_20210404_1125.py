# Generated by Django 3.1.6 on 2021-04-04 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_order'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='supply',
        ),
        migrations.AlterField(
            model_name='order',
            name='num_of_traveller',
            field=models.IntegerField(default=0),
        ),
    ]
