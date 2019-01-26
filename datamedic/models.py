from django.db import models

# Create your models here.

class MedicalRecord(models.Model):
	patient_id = models.CharField('Patient ID', max_length=9)
	patient_name = models.CharField('Name',max_length=50)
	patient_age = models.IntegerField('Age', default=0)
	
	patient_weight = models.CharField('Weight',max_length=20)
	patient_bp = models.CharField('Blood Pressure',max_length=20)
	patient_address = models.CharField('Address', max_length=90)
	registered_date = models.DateTimeField('date registered')

	def __str__(self):
		return(self.patient_id)

class Visitations(models.Model):
	date = models.DateTimeField('Date of appointment') 
	patient_id = models.CharField('Patient ID', max_length=9)
	observations = models.TextField('Observable manifestations')
	findings = models.TextField('Clinical findings')
	plan = models.TextField('Plan')
	drugs_prescribed = models.TextField('Drugs prescribed')

	def __str__(self):
		return(str(self.patient_id) +' visiting on '+ str(self.date))
