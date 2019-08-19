# Generated by Django 2.2.2 on 2019-08-09 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20190808_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analista',
            fields=[
                ('correo', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Asignatario',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('nombre', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='analista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Analista'),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='asignatario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Asignatario'),
        ),
    ]
