# Generated by Django 3.1.6 on 2021-03-22 10:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0007_supply_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supply',
            name='drop_of_before',
            field=models.TimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='supply',
            name='pick_up_from',
            field=models.TimeField(blank=True),
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(blank=True, max_length=50)),
                ('comment', models.CharField(blank=True, max_length=250)),
                ('rate', models.IntegerField(default=1)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(choices=[('New', 'New'), ('True', 'True'), ('False', 'False')], default='True', max_length=10)),
                ('create_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.supply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]