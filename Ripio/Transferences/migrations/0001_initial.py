# Generated by Django 3.2 on 2021-04-22 13:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Accounts', '0001_initial'),
        ('Currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('destination_account', models.CharField(max_length=200, verbose_name='Cuenta de destino')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Cantidad')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency', verbose_name='Moneda')),
                ('origin_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Accounts.account', verbose_name='Cuenta de origen')),
            ],
            options={
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
        ),
    ]
