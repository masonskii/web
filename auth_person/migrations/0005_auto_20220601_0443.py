# Generated by Django 2.1.15 on 2022-06-01 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth_person', '0004_auto_20220531_1820'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='organizate',
            new_name='organizated',
        ),
    ]