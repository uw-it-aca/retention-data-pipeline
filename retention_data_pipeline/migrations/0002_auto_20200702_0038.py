# Generated by Django 2.2.13 on 2020-07-02 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('retention_data_pipeline', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_name_lowc',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='student_no',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
