# Generated by Django 3.2 on 2021-04-17 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.BooleanField(default=True, verbose_name='Estado de cuenta')),
                ('account_number', models.CharField(max_length=200, unique=True, verbose_name='Nº de cuenta')),
                ('alias', models.CharField(max_length=200, unique=True)),
                ('balance', models.FloatField(verbose_name='Saldo')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('type_currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency', verbose_name='Tipo de moneda')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Cuenta',
                'verbose_name_plural': 'Cuentas',
            },
        ),
    ]