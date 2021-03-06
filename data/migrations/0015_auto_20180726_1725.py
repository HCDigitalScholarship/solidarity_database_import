# Generated by Django 2.0.5 on 2018-07-26 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20180726_1530'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='creditunions',
            options={'verbose_name_plural': 'Locations (NCUA)'},
        ),
        migrations.AlterModelOptions(
            name='ncua',
            options={'verbose_name_plural': 'NCUA'},
        ),
        migrations.AlterField(
            model_name='ncua',
            name='oid',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='data.Organizations'),
        ),
    ]
