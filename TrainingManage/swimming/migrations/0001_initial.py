# Generated by Django 3.0.3 on 2020-02-17 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('capacity', models.IntegerField(null=True)),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='groups', to='swimming.Coach')),
            ],
        ),
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('birth_date', models.DateField(null=True)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='trainees', to='swimming.Group')),
            ],
        ),
    ]