# Generated by Django 3.0.4 on 2020-04-04 06:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20200402_0949'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'permissions': (('can_create_author', 'Create new author'),)},
        ),
    ]
