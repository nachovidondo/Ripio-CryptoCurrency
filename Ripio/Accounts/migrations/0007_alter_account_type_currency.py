# Generated by Django 3.2 on 2021-04-20 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Currencies', '0004_alter_currency_price'),
        ('Accounts', '0006_alter_account_type_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='type_currency',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Currencies.currency', verbose_name='Tipo de moneda'),
        ),
    ]