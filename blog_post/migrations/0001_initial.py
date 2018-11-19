# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-19 12:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=300)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=b'')),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('content', models.TextField(verbose_name='Yorum')),
                ('added_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=1)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blogpost_key', to='blog_post.BlogPost')),
            ],
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_key', to='blog_post.Category'),
        ),
    ]