from django.forms import ModelForm
from django import forms
from .models import *

# class VaccinationForm(ModelForm):
# 	class Meta:
# 		model = Person
# 		fields = ['person_ssn','person_email']

class VaccinationForm(forms.Form):
	ssn = forms.IntegerField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'SSN','id':'floatingInput','style': 'margin-bottom: -1px; border-bottom-right-radius: 0; border-bottom-left-radius: 0;'}), label='')
	email = forms.CharField(max_length=70, widget=forms.TextInput(attrs={'class':'form-control	','placeholder':'Email','style':'  margin-bottom: 10px; border-top-left-radius: 0;border-top-right-radius: 0;'}), label='')
	I_want_to_be_vaccinated = forms.BooleanField(widget=forms.TextInput(attrs={'type':'checkbox', 'style':' font-weight: 400; margin-bottom:1em;'}))

class RegistrationForm(forms.Form):
	SSN = forms.IntegerField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'SSN','id':'floatingInput','style': 'margin-bottom: -1px; border-bottom-right-radius: 0; border-bottom-left-radius: 0;'}), label='')
	First_Name = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'First Name','id':'floatingInput','style': 'margin-bottom: -1px;'}), label='')
	Last_Name = forms.CharField(
		widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Last Name','id':'floatingInput','style': 'margin-bottom: -1px;'}), label='')
	Email = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Email','id':'floatingInput','style': 'margin-bottom: -1px;'}), label='')
	Phone = forms.CharField(widget=forms.TextInput(
		attrs={'class':'form-control','placeholder':'Phone','id':'floatingInput','style': 'margin-bottom: -1px; '}), label='')
	Address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control	','placeholder':'Address','style':'  margin-bottom: 10px; border-top-left-radius: 0;border-top-right-radius: 0;'}), label='')

class RegistrationMedicForm(forms.Form):
	ssn = forms.IntegerField()
	medic_type = forms.CharField()
	registry_no = forms.CharField()
	fname = forms.CharField()
	lname = forms.CharField()
	email = forms.CharField()
	phone = forms.CharField()
	addr = forms.CharField()


class PlacesForm(forms.Form):
	place_id = forms.IntegerField()
	name = forms.CharField()
	addr = forms.CharField()

class VaccinesForm(forms.Form):
	name = forms.CharField()
	stock = forms.IntegerField()
	no_of_shots = forms.IntegerField()
	effectivity = forms.FloatField()

class AppointmentForm(forms.Form):
	appointment_id = models.IntegerField(primary_key=True, default=0)
	appointment_date = forms.DateField()

class PlaceHasVaccinesForm(forms.Form):
	stock = forms.IntegerField()
