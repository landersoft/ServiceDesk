# Generated by Django 2.2.2 on 2019-08-08 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0004_auto_20190808_0939'),
    ]

    operations = [
        migrations.CreateModel(
            name='CCMM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ccmm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.CCMM'),
        ),
    ]