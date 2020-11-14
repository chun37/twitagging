# Generated by Django 3.1.3 on 2020-11-13 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('socialaccount', '0003_extra_data_default_dict'),
        ('tagging', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_id', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='socialaccount.socialaccount')),
            ],
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
