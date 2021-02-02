# Generated by Django 3.1.6 on 2021-02-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0003_decimal_field_to_arbitrary_decimal_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_baseline_flag',
            field=models.BooleanField(default=False, verbose_name='Water quality baseline?'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_network_name',
            field=models.CharField(blank=True, db_column='qw_sys_name', max_length=50, verbose_name='Water quality network name'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_sn_flag',
            field=models.BooleanField(default=False, verbose_name='In water quality sub-network?'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_well_chars',
            field=models.CharField(blank=True, choices=[('Background', 'Background'), ('Suspected/Anticipated Changes', 'Suspected/Anticipated Changes'), ('Known Changes', 'Known Changes')], max_length=32, verbose_name='Water quality well characteristics'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_well_purpose',
            field=models.CharField(blank=True, choices=[('Dedicated Monitoring/Observation', 'Dedicated Monitoring/Observation'), ('Other', 'Other')], max_length=32, verbose_name='Water quality well purpose'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_well_purpose_notes',
            field=models.CharField(blank=True, max_length=4000, verbose_name='Water quality well purpose notes'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='qw_well_type',
            field=models.CharField(blank=True, choices=[('Surveillance', 'Surveillance'), ('Trend', 'Trend'), ('Special', 'Special')], max_length=32, verbose_name='Water quality well type'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_baseline_flag',
            field=models.BooleanField(default=False, verbose_name='Water-level baseline?'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_network_name',
            field=models.CharField(blank=True, db_column='wl_sys_name', max_length=50, verbose_name='Water-level network name'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_sn_flag',
            field=models.BooleanField(default=False, verbose_name='In water-level sub-network?'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_well_chars',
            field=models.CharField(blank=True, choices=[('Background', 'Background'), ('Suspected/Anticipated Changes', 'Suspected/Anticipated Changes'), ('Known Changes', 'Known Changes')], max_length=32, verbose_name='Water-level well characteristics'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_well_purpose',
            field=models.CharField(blank=True, choices=[('Dedicated Monitoring/Observation', 'Dedicated Monitoring/Observation'), ('Other', 'Other')], max_length=32, verbose_name='Water-level well purpose'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_well_purpose_notes',
            field=models.CharField(blank=True, max_length=4000, verbose_name='Water-level well purpose notes'),
        ),
        migrations.AlterField(
            model_name='monitoringlocation',
            name='wl_well_type',
            field=models.CharField(blank=True, choices=[('Surveillance', 'Surveillance'), ('Trend', 'Trend'), ('Special', 'Special')], max_length=32, verbose_name='Water-level well type'),
        ),
    ]