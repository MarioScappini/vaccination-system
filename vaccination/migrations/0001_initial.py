# Generated by Django 3.2.3 on 2021-06-16 11:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_ssn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('person_fname', models.CharField(max_length=20)),
                ('person_lname', models.CharField(max_length=50)),
                ('person_email', models.CharField(max_length=70)),
                ('person_phone', models.CharField(max_length=13)),
                ('person_addr', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('place_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('place_name', models.CharField(max_length=30)),
                ('place_addr', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('vaccine_id', models.IntegerField(default=123, primary_key=True, serialize=False, unique=True)),
                ('vaccine_name', models.CharField(max_length=25, unique=True)),
                ('vaccine_stock', models.IntegerField()),
                ('vaccine_no_of_shots', models.IntegerField()),
                ('vaccine_effectivity', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PlaceHasVaccines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.IntegerField()),
                ('place_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccination.place')),
                ('vaccine_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccination.vaccine')),
            ],
        ),
        migrations.CreateModel(
            name='Medic',
            fields=[
                ('medic_ssn', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('medic_type', models.CharField(max_length=25)),
                ('medic_registry_no', models.CharField(max_length=25, unique=True)),
                ('medic_fname', models.CharField(max_length=20)),
                ('medic_lname', models.CharField(max_length=50)),
                ('medic_email', models.CharField(max_length=70)),
                ('medic_phone', models.CharField(max_length=13)),
                ('medic_addr', models.CharField(max_length=100)),
                ('medic_place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vaccination.place')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('shot_no', models.IntegerField()),
                ('appointment_date', models.DateTimeField()),
                ('medic_ssn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.medic')),
                ('patient_ssn', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='vaccination.person')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.place')),
                ('vaccine_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vaccination.vaccine')),
            ],
        ),
    ]
