# Generated by Django 3.2.4 on 2021-07-20 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_descriptive', '0004_rename_preprocessing_column_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='description',
            new_name='algorithm',
        ),
    ]