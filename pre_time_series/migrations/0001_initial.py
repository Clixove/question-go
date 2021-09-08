# Generated by Django 3.2.4 on 2021-09-04 14:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('library', '0003_alter_paper_name'),
        ('task_manager', '0002_auto_20210724_0228'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimeSeries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(blank=True)),
                ('error_message', models.TextField(blank=True)),
                ('time_series_sheet', models.CharField(blank=True, max_length=32)),
                ('label_sheet', models.CharField(blank=True, max_length=32)),
                ('from_datetime', models.DateTimeField(blank=True, null=True)),
                ('to_datetime', models.DateTimeField(blank=True, null=True)),
                ('periods', models.IntegerField(blank=True, null=True)),
                ('cached_dataframe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ts_cache', to='library.paper')),
                ('dataframe', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ts_dataframe', to='library.paper')),
                ('matrix', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ts_matrix', to='library.paper')),
                ('normalizers', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ts_normalizers', to='library.paper')),
                ('step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task_manager.step')),
            ],
            options={
                'verbose_name_plural': 'Time Series',
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('belong_time_series', models.BooleanField(default=True)),
                ('is_date', models.BooleanField(default=False)),
                ('is_index', models.BooleanField(default=False)),
                ('is_score', models.BooleanField(default=False)),
                ('use', models.BooleanField(default=False)),
                ('log', models.BooleanField(default=False)),
                ('diff', models.BooleanField(default=False)),
                ('fill_na_avg', models.BooleanField(default=False)),
                ('algorithm', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pre_time_series.timeseries')),
            ],
        ),
    ]