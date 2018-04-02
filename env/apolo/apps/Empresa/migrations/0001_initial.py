# Generated by Django 2.0.3 on 2018-04-02 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('NIT', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('Nombre_empresa', models.CharField(blank=True, max_length=100)),
                ('Sector', models.CharField(choices=[('Industrial', 'Industria'), ('Servicios', 'Servicio'), ('Comercios', 'Comercio')], default='Comercio', max_length=25)),
                ('Activos', models.CharField(blank=True, max_length=12)),
                ('Numero_empleados', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
