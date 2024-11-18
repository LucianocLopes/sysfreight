# Generated by Django 5.1.1 on 2024-11-18 01:23

import accounts.models
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('usermain_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, verbose_name='Sexo')),
                ('birth_date', models.DateField(verbose_name='Data de Nascimento')),
            ],
            options={
                'verbose_name': 'Perfil do Usuário',
                'verbose_name_plural': 'Perfils dos Usuários',
            },
            bases=('accounts.usermain',),
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
