# Generated by Django 3.2 on 2022-07-21 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EmployeeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='DateOfJoining',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='employee',
            name='Department',
            field=models.CharField(max_length=500),
        ),
    ]
