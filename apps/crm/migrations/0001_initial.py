# Generated by Django 2.2 on 2019-05-25 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoActividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Tipo de Actividad',
                'verbose_name_plural': 'Tipos de Actividad',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=80, verbose_name='Nombre')),
                ('apellidos', models.CharField(max_length=80, verbose_name='Nombre')),
                ('cargo', models.CharField(max_length=80, verbose_name='Nombre')),
                ('telefono', models.CharField(max_length=80, verbose_name='Nombre')),
                ('celular', models.CharField(max_length=80, verbose_name='Nombre')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
                'ordering': ['apellidos', 'nombre'],
            },
        ),
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(verbose_name='Descripción')),
                ('accion', models.TextField(verbose_name='Acciones')),
                ('fecha', models.DateField(verbose_name='Fecha')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.Cliente')),
                ('tipo', models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='crm.TipoActividad')),
            ],
            options={
                'verbose_name': 'Actividad',
                'verbose_name_plural': 'Actividades',
                'ordering': ['fecha', 'cliente', 'tipo'],
            },
        ),
    ]
