# Generated by Django 5.0.4 on 2024-04-09 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_management_app', '0008_staffs_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staffs',
            name='first_name',
            field=models.CharField(max_length=50),
        ),
    ]
