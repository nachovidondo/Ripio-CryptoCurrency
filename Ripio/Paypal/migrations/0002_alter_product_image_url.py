# Generated by Django 3.2 on 2021-04-20 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Paypal', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image_url',
            field=models.ImageField(blank=True, default=True, null=True, upload_to=''),
        ),
    ]
