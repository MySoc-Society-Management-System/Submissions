# Generated by Django 3.2 on 2021-04-28 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_appartment_dependents_employee_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='Status',
            field=models.CharField(default='Pending', max_length=50),
        ),
    ]
