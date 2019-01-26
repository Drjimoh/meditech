from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='homepage'),
	path('/<int:patient_id>/patient/', views.patient_record, name='patientpage' ),
	path('/login/', views.login_page, name='loginpage'),

]

