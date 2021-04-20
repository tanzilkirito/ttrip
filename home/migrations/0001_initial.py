# Generated by Django 3.1.6 on 2021-03-19 16:34

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_keyword', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
                ('overview', ckeditor_uploader.fields.RichTextUploadingField()),
                ('image1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]