# Generated by Django 2.2.5 on 2020-03-04 14:23

import datetime
from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('phone_no', models.IntegerField()),
                ('address', models.CharField(blank=True, max_length=30)),
                ('profile_pic', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='UserReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.IntegerField()),
                ('sex', models.IntegerField(choices=[(1, 'Male'), (0, 'Female'), (0, 'Others')])),
                ('cp', models.IntegerField(choices=[(1, 'Typical Angina'), (2, 'Atypical Angina'), (3, 'Non-Anignal Pain'), (4, 'Asymptotic')])),
                ('restbps', models.IntegerField()),
                ('chol', models.IntegerField()),
                ('fbs', models.IntegerField(choices=[(0, 'Blood Sugar < 120mg/dl'), (1, 'Blood Sugar > 120mg/dl')])),
                ('ecg', models.IntegerField(choices=[(0, 'Normal'), (1, 'Having ST-T Wave Abromality'), (2, 'Left Ventricular Hyperthrophy')])),
                ('heart_rate', models.IntegerField()),
                ('ex_in_angina', models.IntegerField(choices=[(1, 'Yes'), (0, 'No')])),
                ('st_depression_in_exercise', models.FloatField()),
                ('peak_st_segment', models.IntegerField(choices=[(1, 'Upsloping'), (2, 'Flat'), (3, 'Downsloping')])),
                ('vessels_by_flourosopy', models.FloatField()),
                ('thal', models.IntegerField(choices=[(3, 'Normal'), (6, 'Fixed Defect'), (7, 'Reversible Defect')])),
                ('date_time', models.DateTimeField(default=datetime.datetime(2020, 3, 4, 14, 23, 4, 494061, tzinfo=utc))),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
