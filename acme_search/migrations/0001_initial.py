# Generated by Django 3.1 on 2020-08-15 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('company', models.CharField(default='', max_length=100)),
                ('emails', models.CharField(default='', max_length=100)),
                ('phones', models.CharField(default='', max_length=100)),
                ('matching_terms', models.CharField(default='', max_length=100)),
                ('last_contact', models.CharField(default='', max_length=100)),
            ],
        ),
    ]
