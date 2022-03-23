# Generated by Django 4.0.2 on 2022-03-11 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_person', '0011_alter_person_card'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toCardFromUser', to='auth_person.personcard'),
        ),
        migrations.AlterField(
            model_name='personcard',
            name='secret_code',
            field=models.CharField(max_length=3, unique=True),
        ),
    ]
