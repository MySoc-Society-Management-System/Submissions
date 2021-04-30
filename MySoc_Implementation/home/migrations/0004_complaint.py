# Generated by Django 3.2 on 2021-04-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_name_contact_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ownername', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('appartment', models.CharField(max_length=10)),
                ('desc', models.CharField(max_length=500)),
                ('date', models.DateField()),
            ],
        ),
    ]
