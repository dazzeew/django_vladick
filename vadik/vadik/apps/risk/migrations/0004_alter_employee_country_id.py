# Generated by Django 4.0.6 on 2022-07-16 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('risk', '0003_alter_employee_country_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='country_id',
            field=models.ForeignKey(blank=True, db_column='country_id', on_delete=django.db.models.deletion.PROTECT, to='risk.country', verbose_name='Страна'),
        ),
    ]
