# Generated by Django 5.0.3 on 2024-04-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('sl_no', models.AutoField(primary_key=True, serialize=False)),
                ('desig', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('Qualification', models.CharField(max_length=10)),
                ('assigned_work', models.CharField(max_length=1000)),
                ('ofc_entry', models.DateTimeField()),
                ('ofc_out', models.DateTimeField()),
            ],
            options={
                'db_table': 'Staff_tracking',
            },
        ),
    ]
