# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-13 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import parler.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='', help_text='Please provide an internal code for this color.', max_length=32, unique=True, verbose_name='code')),
            ],
            options={
                'verbose_name': 'color',
                'verbose_name_plural': 'colors',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='ColorTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('name', models.CharField(default='', help_text='Please provide a name for this color.', max_length=32, verbose_name='name')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='i18n.Color')),
            ],
            options={
                'db_tablespace': '',
                'managed': True,
                'db_table': 'i18n_color_translation',
                'verbose_name': 'color Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Nationality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country_code', models.CharField(default='', help_text='Please provide the ISO 2-letter country-code for this nationality.', max_length=2, unique=True, verbose_name='country code')),
            ],
            options={
                'verbose_name': 'nationality',
                'verbose_name_plural': 'nationalities',
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name='NationalityTranslation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code', models.CharField(db_index=True, max_length=15, verbose_name='Language')),
                ('label', models.CharField(default='', help_text='Please provide a label for this nationality.', max_length=32, verbose_name='label')),
                ('master', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='i18n.Nationality')),
            ],
            options={
                'db_tablespace': '',
                'managed': True,
                'db_table': 'i18n_nationality_translation',
                'verbose_name': 'nationality Translation',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='Please provide a name.', max_length=32, verbose_name='name')),
                ('favorite_color', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='i18n.Color')),
                ('nationality', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='i18n.Nationality')),
            ],
            options={
                'verbose_name': 'person',
                'verbose_name_plural': 'people',
            },
        ),
        migrations.AlterUniqueTogether(
            name='nationalitytranslation',
            unique_together=set([('language_code', 'master')]),
        ),
        migrations.AlterUniqueTogether(
            name='colortranslation',
            unique_together=set([('language_code', 'master')]),
        ),
    ]