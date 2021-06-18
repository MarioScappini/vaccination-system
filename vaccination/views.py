from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .forms import *
from .models import *
import logging
import datetime
import random 
from datetime import date, timedelta
from django.utils import timezone

class IndexView(TemplateView):
	template_name = 'index.html'
	
	def get(self, request):
		form = VaccinationForm()
		return render(request,self.template_name,{'form':form})

	def post(self,request):
		form = VaccinationForm(request.POST)
		if form.is_valid():
			ssn = form.cleaned_data['ssn']
			email = form.cleaned_data['email']
			query = Person.objects.filter(person_ssn=ssn)
			if query.exists():
				if email == query[0].person_email:
					redirect_address = '/appointment/'+str(ssn)
					return redirect(redirect_address)
				else:
					return render(request,self.template_name,{'form':form, 
															'message':"Incorrect Mail"})
			else:
				return redirect('/register')
		else:
			return render(request,self.template_name,{'form':form, 'message':"Incorrect Input"})

class PlacesView(TemplateView):
	template_name = 'place.html'
	def get(self, request, ssn):
		persons_appointments = Appointment.objects.filter(patient_ssn=ssn)
		if persons_appointments.exists():
			if persons_appointments.last().appointment_date < timezone.make_aware(datetime.datetime.now()):

				applied_vaccine = persons_appointments.last().vaccine_name
				if applied_vaccine.vaccine_no_of_shots > persons_appointments.last().shot_no:
					places = Place.objects.all()
					return render(request, self.template_name,{'places':places,'ssn':str(ssn),'appointments':persons_appointments, 'dose':2})
				else:
					return render(request, self.template_name,{'appointments':persons_appointments})
			else:
				return render(request, self.template_name,{'appointments':persons_appointments})
		
		places = Place.objects.all()
		return render(request, self.template_name,{'places':places, 'ssn':str(ssn),'dose':1})

class PlaceWithVaccineView(TemplateView):
	template_name = 'place_w_vaccines.html'
	def get(self, request,ssn, dose,place_id):
		persons_appointments = Appointment.objects.filter(patient_ssn=ssn)
		if persons_appointments.exists():
			available_vaccines = PlaceHasVaccines.objects.filter(place_id=place_id,stock__gt=0, vaccine_id=persons_appointments.last().vaccine_name)
		else:
			available_vaccines = PlaceHasVaccines.objects.filter(place_id=place_id,stock__gt=0)
		return render(request, self.template_name,{'available_vaccines':available_vaccines, 'place_id':place_id , 'ssn':ssn,'dose':dose})

class AppointmentView(TemplateView):
	template_name = 'appointment-list.html'

	def post(self,request,ssn,dose,place_id,vaccine_id):
		date = request.POST['date']

		medic = Medic.objects.get(medic_ssn=request.POST['medic_ssn'])
		person = Person.objects.get(person_ssn=ssn)
		vaccine = Vaccine.objects.get(vaccine_id=vaccine_id)
		place = Place.objects.get(place_id=place_id)
		appointment_id = int(str(ssn)+str(dose))
		q = Appointment(appointment_id=appointment_id,
						shot_no=dose,
						appointment_date=date,
						patient_ssn=person,
						medic_ssn=medic,
						vaccine_name=vaccine,
						place=place)
		q.save()
		no_vaccines_in_place = PlaceHasVaccines.objects.get(place_id=place_id, vaccine_id=vaccine_id)
		no_vaccines_in_place.stock = no_vaccines_in_place.stock -1
		no_vaccines_in_place.save()
		no_vaccines = Vaccine.objects.get(vaccine_id=vaccine_id)
		no_vaccines.vaccine_stock = no_vaccines.vaccine_stock -1
		no_vaccines.save()
		return render(request, 'sucess.html')

	def get(self,request,ssn,dose,place_id,vaccine_id):
			
		medics = Medic.objects.filter(medic_place=place_id)
		packet = []
		for medic in medics:
			times = [datetime.time(8,0,0),
					datetime.time(10,0,0),
					datetime.time(12,0,0)]
			available_datetime = []
			appointments_list = Appointment.objects.filter(medic_ssn=medic.medic_ssn)
			delta = date(2021,7,1) - date(2021,6,1) 
			for i in range(delta.days + 1):
				day = date(2021,6,1)  + timedelta(days=i)
				for time in times:
					available_datetime.append(timezone.make_aware(datetime.datetime.combine(day,time)))
			
			for appointment in appointments_list:
				available_datetime.remove(appointment.appointment_date)

			packet.append([medic,available_datetime])
		return render(request,self.template_name,{'appointments':packet,
												'place':place_id,
												'vaccine':vaccine_id,})

class RegisterView(TemplateView):
	template_name = 'register.html'

	def get(self, request):
		form = RegistrationForm()
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = RegistrationForm(request.POST)
		if form.is_valid():
			ssn = form.cleaned_data['SSN']
			fname = form.cleaned_data['First_Name']
			lname = form.cleaned_data['Last_Name']
			email = form.cleaned_data['Email']
			phone = form.cleaned_data['Phone']
			addr = form.cleaned_data['Address']
			q = Person(person_ssn=ssn,person_fname=fname,person_lname=lname,person_email=email,person_phone=phone,person_addr=addr)
			q.save()
			redirect_address = '/appointment/'+str(ssn)
		return render(request, self.template_name,
			{'form':form,
			'message':"Registration was completed succesfully",
			'url':redirect_address})
