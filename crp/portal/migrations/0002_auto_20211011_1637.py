# Generated by Django 3.0.8 on 2021-10-11 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='applied_jobs',
            new_name='AppliedJobs',
        ),
        migrations.RenameModel(
            old_name='comp_details',
            new_name='CompanyDetails',
        ),
        migrations.RenameModel(
            old_name='job_pos',
            new_name='JobPosition',
        ),
        migrations.RenameModel(
            old_name='stu_details',
            new_name='StudentDetails',
        ),
    ]
