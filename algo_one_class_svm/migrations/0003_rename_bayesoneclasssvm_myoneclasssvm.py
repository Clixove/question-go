# Generated by Django 3.2.9 on 2021-11-18 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task_manager', '0004_auto_20210916_1126'),
        ('library', '0003_alter_paper_name'),
        ('algo_one_class_svm', '0002_auto_20211118_1609'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BayesOneClassSVM',
            new_name='MyOneClassSVM',
        ),
    ]