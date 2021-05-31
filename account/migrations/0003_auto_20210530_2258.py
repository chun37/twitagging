# Generated by Django 3.2.3 on 2021-05-30 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0002_auto_20210530_2255"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_admin",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="user",
            name="display_name",
            field=models.CharField(default="", max_length=255),
        ),
        migrations.AlterField(
            model_name="user",
            name="screen_name",
            field=models.CharField(default="", max_length=255),
        ),
    ]
