# Generated by Django 4.1.5 on 2023-01-06 23:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(name="Contact",),
    ]
