# Generated by Django 4.0.5 on 2022-06-02 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_person', '0010_person_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comm',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='organization',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]