# Generated by Django 2.0 on 2019-12-03 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='emil',
            new_name='email',
        ),
    ]