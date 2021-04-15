# Generated by Django 3.2 on 2021-04-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nombre')),
                ('surname', models.CharField(blank=True, max_length=200, null=True, verbose_name='Apellido')),
                ('creation_date', models.DateTimeField(auto_now=True, verbose_name='Fecha')),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile/', verbose_name='Imagen de perfil')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]