# Generated by Django 5.0.2 on 2024-06-17 04:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_rename_p_duration_project_p_projectname_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_certificate', models.CharField(max_length=500)),
                ('c_year', models.CharField(max_length=500)),
                ('cv', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cv')),
            ],
        ),
    ]
