# Generated by Django 4.0 on 2022-03-03 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_person', '0004_alter_logo_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='personId',
        ),
        migrations.RemoveField(
            model_name='mobilephone',
            name='personId',
        ),
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_person.email'),
        ),
        migrations.AddField(
            model_name='person',
            name='phone',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth_person.mobilephone'),
        ),
    ]
