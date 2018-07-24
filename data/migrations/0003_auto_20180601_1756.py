# Generated by Django 2.0.5 on 2018-06-01 17:56

from django.db import migrations, models


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('data', '0002_auto_20180601_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='address2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='country',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='county',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='geographic_location',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='lid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='location_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='match_addr',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='oid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='primary_loc',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='ref_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='side',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='zipcode',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
