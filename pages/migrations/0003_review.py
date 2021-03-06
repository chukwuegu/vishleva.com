# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-01-16 13:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0010_auto_20160105_1307'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0015_event_notified_at'),
        ('pages', '0002_galleryextended'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('text', models.TextField(db_index=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Client')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages_review_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pages_review_modified_by', to=settings.AUTH_USER_MODEL)),
                ('photos', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='photologue.Photo')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
    ]
