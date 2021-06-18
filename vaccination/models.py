from django.db import models

class Person(models.Model):
    person_ssn = models.IntegerField(primary_key=True,unique=True)
    person_fname = models.CharField(max_length=20)
    person_lname = models.CharField(max_length=50)
    person_email = models.CharField(max_length=70)
    person_phone = models.CharField(max_length=13)
    person_addr = models.CharField(max_length=100)

    def __str__(self):
        text = str(self.person_ssn) + ' ' + str(self.person_fname) + ' ' + self.person_lname
        return text

class Place(models.Model):
    place_id = models.IntegerField(primary_key=True,unique=True)
    place_name = models.CharField(max_length=30)
    place_addr = models.CharField(max_length=50)

    def __str__(self):
        return self.place_name


class Vaccine(models.Model):
    vaccine_id = models.IntegerField(primary_key=True, unique=True, default=123)
    vaccine_name = models.CharField(max_length=25, unique=True)
    vaccine_stock = models.IntegerField()
    vaccine_no_of_shots = models.IntegerField()
    vaccine_effectivity = models.FloatField()

    def __str__(self):
        return self.vaccine_name

class Medic(models.Model):
    medic_ssn = models.IntegerField(primary_key=True,unique=True)
    medic_type = models.CharField(max_length=25)
    medic_registry_no = models.CharField(max_length=25, unique=True)
    medic_fname = models.CharField(max_length=20)
    medic_lname = models.CharField(max_length=50)
    medic_email = models.CharField(max_length=70)
    medic_phone = models.CharField(max_length=13)
    medic_addr = models.CharField(max_length=100)
    medic_place = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        text = str(self.medic_ssn) + ' ' + str(self.medic_fname) + ' ' + str(self.medic_lname)
        return text

class PlaceHasVaccines(models.Model):
    stock = models.IntegerField()
    place_id = models.ForeignKey(Place, on_delete=models.SET_NULL, null=True)
    vaccine_id = models.ForeignKey(Vaccine, on_delete=models.SET_NULL, null=True)

class Appointment(models.Model):
    appointment_id = models.IntegerField(primary_key=True, default=0)
    shot_no = models.IntegerField()
    appointment_date = models.DateTimeField()
    patient_ssn = models.ForeignKey(Person,on_delete=models.CASCADE, null=True)
    medic_ssn = models.ForeignKey(Medic, on_delete=models.CASCADE)
    vaccine_name = models.ForeignKey(Vaccine, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
