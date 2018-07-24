# Generated by Django 2.0.5 on 2018-06-06 16:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    atomic = False
    dependencies = [
        ('data', '0004_auto_20180604_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lid', models.IntegerField(null=True)),
                ('name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100, null=True)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('fax', models.CharField(max_length=50, null=True)),
                ('email', models.CharField(max_length=100, null=True)),
                ('uid', models.IntegerField(null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='data',
            name='lid',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='oid',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='oid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.Data'),
        ),
    ]
