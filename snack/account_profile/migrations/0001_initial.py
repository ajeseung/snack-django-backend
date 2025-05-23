# Generated by Django 5.1.7 on 2025-05-14 14:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountProfile',
            fields=[
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='account.account')),
                ('account_name', models.CharField(blank=True, max_length=100, null=True)),
                ('account_nickname', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_num', models.CharField(blank=True, max_length=255, null=True)),
                ('account_add', models.CharField(blank=True, max_length=255, null=True)),
                ('account_sex', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female'), ('Other', 'Other')], max_length=10, null=True)),
                ('account_birth', models.CharField(blank=True, max_length=100, null=True)),
                ('account_pay', models.JSONField(blank=True, null=True)),
                ('account_sub', models.BooleanField(default=False)),
                ('account_age', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'account_profile',
            },
        ),
    ]
