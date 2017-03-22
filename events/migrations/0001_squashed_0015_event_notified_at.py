# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-18 17:57
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import vishleva.models


class Migration(migrations.Migration):

    replaces = [('events', '0001_initial'), ('events', '0002_auto_20161118_1137'), ('events', '0003_auto_20161118_1151'), ('events', '0004_auto_20161118_1155'), ('events', '0005_auto_20161118_1200'), ('events', '0006_auto_20161118_1201'), ('events', '0007_auto_20161120_1022'), ('events', '0008_auto_20161120_1050'), ('events', '0007_auto_20161118_1817'), ('events', '0009_merge_20161121_1557'), ('events', '0010_auto_20161121_1602'), ('events', '0011_event_status'), ('events', '0012_event_google_calendar_id'), ('events', '0013_auto_20161201_1050'), ('events', '0014_event_expenses'), ('events', '0015_event_notified_at')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.TextField(blank=True, null=True)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=30)),
                ('email', models.EmailField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_client_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_client_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_at', models.DateTimeField(auto_now=True, null=True)),
                ('comment', models.TextField(blank=True, db_index=True, null=True)),
                ('begin', models.DateTimeField(db_index=True)),
                ('end', models.DateTimeField(db_index=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('total', models.PositiveIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('paid', models.PositiveIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='events', to='events.Client')),
                ('created_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_event_created_by', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='events_event_modified_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(db_index=True, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='first_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], db_index=True, max_length=1),
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='client',
            name='patronymic',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='comment',
            field=models.TextField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.EmailField(blank=True, db_index=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['begin']},
        ),
        migrations.AlterField(
            model_name='client',
            name='last_name',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=30, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=vishleva.models.NullableEmailField(blank=True, db_index=True, max_length=200, null=True, unique=True),
        ),
        migrations.AlterModelOptions(
            name='client',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AddField(
            model_name='client',
            name='social_url',
            field=models.URLField(blank=True, help_text='social profile url (vk, facebook, ect)', max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(db_index=True, max_length=30, unique=True),
        ),
        migrations.AddField(
            model_name='event',
            name='status',
            field=models.CharField(choices=[('not_confirmed', 'not confirmed'), ('open', 'open'), ('closed', 'closed')], db_index=True, default='open', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='google_calendar_id',
            field=models.CharField(blank=True, db_index=True, help_text='google calendar event id', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='expenses',
            field=models.PositiveIntegerField(db_index=True, default=0, validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AddField(
            model_name='event',
            name='notified_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]