# Generated by Django 2.2 on 2020-09-12 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='titile',
            new_name='title',
        ),
    ]
