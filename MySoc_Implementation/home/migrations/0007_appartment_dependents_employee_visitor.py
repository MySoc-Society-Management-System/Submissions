# Generated by Django 3.2 on 2021-04-28 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bills'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appartmentno', models.CharField(max_length=10)),
                ('ownerid', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=15)),
                ('dependentsno', models.CharField(max_length=15)),
                ('vacancy', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Dependents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('ownerid', models.CharField(max_length=10)),
                ('appartment', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
                ('email', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employeeid', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=122)),
                ('salamount', models.CharField(max_length=10)),
                ('salstatus', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.CharField(max_length=122)),
            ],
        ),
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('arrival', models.DateTimeField()),
                ('departure', models.DateTimeField()),
                ('ownerid', models.CharField(max_length=10)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
    ]