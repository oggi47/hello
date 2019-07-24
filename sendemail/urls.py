# sendemail/urls.py
from django.contrib import admin
from django.urls import path

from .views import successView,business_travel_1,business_travel_1,business_public_liability_2,business_working_injury_compensation_3,business_property_all_risks_4,business_directors_and_officers_5,business_foreign_worker_medical_6,business_security_bond_7,business_cyber_risk_8,personal_travel_3,personal_car_2,personal_home_1

urlpatterns = [
    
    path('success/', successView, name='success'),
    path('business_travel/' ,business_travel_1,name='business_travel'),
    path('business_public_liability/',business_public_liability_2,name="business_public_liability"),
    path('business_working_injury_compensation/',business_working_injury_compensation_3,name="business_working_injury_compensation"),
    path('business_property_all_risks/',business_property_all_risks_4,name="business_property_all_risks"),
    path('business_directors_and_officers/',business_directors_and_officers_5,name="business_directors_and_officers"),
    path('business_foreign_worker_medical/',business_foreign_worker_medical_6,name="business_foreign_worker_medical"),
    path('business_security_bond/',business_security_bond_7,name="business_security_bond"),
    path('business_cyber_risk/',business_cyber_risk_8,name="business_cyber_risk"),
    path('personal_home/',personal_home_1,name="personal_home"),
    path('personal_car/',personal_car_2,name="personal_car"),
    path('personal_travel/',personal_travel_3,name="personal_travel"),
   
]