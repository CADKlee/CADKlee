# Generated by Django 3.2.7 on 2021-11-08 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CAD_Klee', '0003_auto_20211108_1037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientes',
            old_name='user',
            new_name='usuario',
        ),
        migrations.RenameField(
            model_name='produtos',
            old_name='user',
            new_name='usuario',
        ),
    ]
