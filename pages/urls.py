from django.urls import path

from .views import HomePageView , BusinessPageView, PersonalPageView,FormBisPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    
    path('personal', PersonalPageView.as_view(), name='personal'),
    path('bisform', FormBisPageView.as_view(), name='bisform'),
    path('business_oggi' ,BusinessPageView.as_view(),name='business_oggi')
]