# Generated by Django 4.0.6 on 2022-07-12 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0011_auto_20220713_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='count',
            field=models.FloatField(verbose_name='Сумма перевода'),
        ),
    ]
