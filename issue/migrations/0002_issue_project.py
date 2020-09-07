# Generated by Django 3.1 on 2020-09-07 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('issue', '0001_initial'),
        ('project_management', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.project'),
        ),
    ]
