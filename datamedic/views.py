from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.conf import settings
from .models import MedicalRecord





def patient_list(request):
	patient_list = MedicalRecord.objects.all()
	return render(request, 'templates/home.html', {'patient_list':patient_list})


def index(request):
	return HttpResponse("Welcome home to DataMedic, access your Patient's medical records with their identification numbers")

def patient_record(request, patient_id):
	if request.user.is_authenticated:
		return HttpResponse("%d has the following medical record with us " %patient_id)
	else:
		return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))

def login_page(request):
	username = request.POST.get('username')
	password = request.POST.get('password')
	user = authenticate(request, username=username, password=password)
	if user is not None:
		login(request, user)
		response = redirect(patient_record)
		return response
	else:
		response = redirect(index)
		return response


# Create your views here.
