# Generated by Django 2.2.2 on 2019-08-09 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0009_auto_20190809_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='grupo_resolutor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Grupo'),
        ),
    ]