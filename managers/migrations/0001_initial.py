# Generated by Django 3.0.4 on 2020-03-07 05:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('designation', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=50)),
                ('is_available', models.BooleanField(default=True)),
                ('hire_date', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('work', models.CharField(choices=[('Plumber', 'Efficient in Plumbing work'), ('electrician', 'Efficient in handling electircal work'), ('House_maid', 'For household activities')], default='House_maid', max_length=200)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=20)),
                ('is_availabe', models.BooleanField(default=True)),
                ('hire_date', models.DateTimeField(default=datetime.datetime.now)),
                ('photo', models.ImageField(blank=True, upload_to='')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='managers.Manager')),
            ],
        ),
    ]