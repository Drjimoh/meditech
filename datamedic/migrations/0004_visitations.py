# Generated by Django 2.1.5 on 2019-01-25 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datamedic', '0003_auto_20190125_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='Date of appointment')),
                ('observations', models.TextField(verbose_name='Observable manifestations')),
                ('findings', models.TextField(verbose_name='Clinical findings')),
                ('plan', models.TextField(verbose_name='Plan')),
                ('drugs_prescribed', models.TextField(verbose_name='Drugs prescribed')),
            ],
        ),
    ]
