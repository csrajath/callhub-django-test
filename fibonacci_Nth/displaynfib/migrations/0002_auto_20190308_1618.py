# Generated by Django 2.1.7 on 2019-03-08 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('displaynfib', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fiboutput',
            old_name='num',
            new_name='number',
        ),
    ]
