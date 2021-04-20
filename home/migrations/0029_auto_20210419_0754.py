# Generated by Django 3.1.6 on 2021-04-19 07:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0028_auto_20210419_1312'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='message',
        ),
        migrations.RemoveField(
            model_name='message',
            name='supply',
        ),
        migrations.RemoveField(
            model_name='message',
            name='time',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user',
        ),
        migrations.AddField(
            model_name='message',
            name='fromUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='fromUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='location',
            field=models.CharField(blank=True, default='', max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='message',
            name='toUser',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='toUser', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='message',
            name='update_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
