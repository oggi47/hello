from django.shortcuts import render

from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'home.html'

class BusinessPageView(TemplateView):
	template_name = 'business_oggi.html'

class PersonalPageView(TemplateView):
	template_name = 'personal.html'

class FormBisPageView(TemplateView):
	template_name = 'bisform.html'

