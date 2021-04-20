# Generated by Django 3.2 on 2021-04-19 14:19

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Currencies', '0003_currency_update_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Accounts', '0002_alter_account_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='account',
            unique_together={('username', 'type_currency')},
        ),
    ]