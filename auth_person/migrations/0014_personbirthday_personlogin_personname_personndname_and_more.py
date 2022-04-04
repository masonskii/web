# Generated by Django 4.0.2 on 2022-04-03 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_person', '0013_alter_person_card_alter_personcard_secret_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonBirthday',
            fields=[
                ('birthday_id', models.AutoField(primary_key=True, serialize=False)),
                ('birthday', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonLogin',
            fields=[
                ('login_id', models.AutoField(primary_key=True, serialize=False)),
                ('login', models.CharField(help_text='basic login information', max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonName',
            fields=[
                ('name_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonNdName',
            fields=[
                ('ndName_id', models.AutoField(primary_key=True, serialize=False)),
                ('ndName', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PersonPassword',
            fields=[
                ('password_id', models.AutoField(primary_key=True, serialize=False)),
                ('password', models.CharField(help_text='basic login information', max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PersonSurname',
            fields=[
                ('surname_id', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.EmailField(blank=True, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toEmailFromUser', to='auth_person.email'),
        ),
        migrations.AlterField(
            model_name='person',
            name='birthday',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toBurthdayFromUser', to='auth_person.personbirthday'),
        ),
        migrations.AlterField(
            model_name='person',
            name='login',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toLoginFromUser', to='auth_person.personlogin'),
        ),
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toNameFromUser', to='auth_person.personname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='ndName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toNdNameFromUser', to='auth_person.personndname'),
        ),
        migrations.AlterField(
            model_name='person',
            name='password',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='toPasswordFromUser', to='auth_person.personpassword'),
        ),
        migrations.AlterField(
            model_name='person',
            name='surname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='toSurnameFromUser', to='auth_person.personsurname'),
        ),
    ]