# Generated by Django 2.1.5 on 2019-01-25 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datamedic', '0002_visitations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitations',
            name='medicalrecord_ptr',
        ),
        migrations.DeleteModel(
            name='Visitations',
        ),
    ]