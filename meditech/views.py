from django.http import HttpResponse 
import datetime 
import random



def welcome(request):
	patient_id = int(234678)
	html="<html><body>Welcome  %d . <p>What would you like to do ? </p> <br><a href='records/'>My Records</a> </body> </html> " %patient_id
	return HttpResponse(html)


def patient_record(request):
	record = '''The following are your most recent medical records:
	Dec 2018
	Aug 2018
	Jan 2018
	July 2017
	Dec 2015 '''
	html = "<html><body>%s </body> </html> " %record
	return HttpResponse(html)
