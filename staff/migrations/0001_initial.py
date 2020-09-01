# Generated by Django 3.1 on 2020-09-01 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project_management', '0001_initial'),
        ('user', '0002_organisation'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_management.project')),
            ],
        ),
        migrations.CreateModel(
            name='StaffSubType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=8)),
                ('staff_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffcategory')),
            ],
        ),
        migrations.CreateModel(
            name='StaffAttendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('staff_count', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('staff_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staff.staffsubtype')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.user')),
            ],
        ),
    ]
