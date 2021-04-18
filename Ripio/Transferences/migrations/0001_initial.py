# Generated by Django 3.2 on 2021-04-17 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Currencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('origin_account', models.CharField(max_length=200, verbose_name='Cuenta de origen')),
                ('destination_account', models.CharField(max_length=200, verbose_name='Cuenta de destino')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('amount', models.FloatField(verbose_name='Cantidad')),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency', verbose_name='Moneda')),
            ],
            options={
                'verbose_name': 'Transferencia',
                'verbose_name_plural': 'Transferencias',
            },
        ),
    ]