# sendemail/views.py
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import Travel_Form,Public_Liability_Form,Working_Injury_Compensation,Property_All_Risks,Directors_and_Officers,Foreign_Worker_Medical,Security_Bond,Cyber_Risk,Home_P,Car_P
from django.views.generic import TemplateView
from django.shortcuts import render_to_response
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render
from django.template.response import TemplateResponse
def business_travel_1(request):
      
     if request.method=='POST':
        travel_form = Travel_Form(request.POST)
        if travel_form.is_valid():
            
            subject ="travel_form"
            from_email ='pinkxyro@Gmail.com'
            subject='travel_form'
            data = request.POST.copy()
            form=data
            context={'form':form,'data':data}
            email_body = render_to_string("business_travel_EMAIL.html", context)
            
            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_travel_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send()                      
            travel_form = Travel_Form()
           
            return redirect('success')

     return render(request, "business_travel.html", {'travel_form': Travel_Form})
def business_public_liability_2(request):
    if request.method=='POST':
        public_liability_form=Public_Liability_Form(request.POST)
        if public_liability_form.is_valid():
           form=Public_Liability_Form()
           
          
           from_email ='pinkxyro@Gmail.com'
           subject ="public_liabiltiy_form"
           data = request.POST.copy()
           form=data    
           
           context= {'form': form, 'data':data}        
           email_body = render_to_string("public_liability_EMAIL.html", context)
          
           message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com'])
           html_template=get_template(settings.BASE_DIR +"/templates/public_liability_EMAIL.html").render()
           message.attach_alternative(email_body,"text/html")
           message.send()                      
           public_liability_form = Public_Liability_Form()
              
           return redirect('success')
           
    return render(request, "business_public_liability.html", {'public_liability_form':Public_Liability_Form})
    

def business_working_injury_compensation_3(request):
    if request.method == 'POST':
        working_injury_compensation=Working_Injury_Compensation(request.POST)
        if working_injury_compensation.is_valid():
            
            subject ="Working_Injury_Compensation"
            from_email ='pinkxyro@Gmail.com'
            data = request.POST.copy()
            context={'form':form,'data':data}
            form=data 
            email_body = render_to_string("business_working_injury_compensation_EMAIL.html", context)
            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_working_injury_compensation_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send()                      
            working_injury_compensation = Working_Injury_Compensation()
            
            return redirect('success')
    return render(request, "business_working_injury_compensation.html", {'working_injury_compensation':Working_Injury_Compensation})

def business_property_all_risks_4(request):
    if request.method == 'POST':
        property_all_risks=Property_All_Risks(request.POST)
    
        if property_all_risks.is_valid():
            
            subject ="Property All Risks"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            data = request.POST.copy()
            context={'form':form,'data':data}
            email_body = render_to_string("business_property_all_risks_EMAIL.html", context)
            
        
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_property_all_risks_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            property_all_risks=Property_All_Risks()            
            return redirect('success')

    return render(request,"business_property_all_risks.html",{ 'property_all_risks':Property_All_Risks})

def business_directors_and_officers_5(request):
    if request.method == 'POST':    
    
        directors_and_officers=Directors_and_Officers(request.POST)
        if directors_and_officers.is_valid():
            
            subject ="Directors and Officers"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("business_directors_and_officers_EMAIL.html", context)
            

            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_directors_and_officers_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            directors_and_officers=Directors_and_Officers()          
            return redirect('success')
    return render(request, "business_directors_and_officers.html", {'directors_and_officers':Directors_and_Officers})

def business_foreign_worker_medical_6(request):
    if request.method == 'POST':
        foreign_worker_medical=Foreign_Worker_Medical(request.POST)     
        
        if foreign_worker_medical.is_valid():
            
            subject ="Foreign Worker Medical"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("business_foreign_worker_medical_EMAIL.html", context)    
           

            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_foreign_worker_medical_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            foreign_worker_medical=Foreign_Worker_Medical()
            
            return redirect('success')
    return render(request, "business_foreign_worker_medical.html", {'foreign_worker_medical':Foreign_Worker_Medical})

def business_security_bond_7(request):
    if request.method == 'POST':       
    
        security_bond=Security_Bond(request.POST)
        if security_bond.is_valid():
           
            subject ="Security Bond"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("business_security_bond_EMAIL.html", context)    
            

            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_security_bond_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            security_bond=Security_Bond()
           
            return redirect('success')
    return render(request, "business_security_bond.html", {'security_bond':Security_Bond})

def business_cyber_risk_8(request):
    if request.method == 'POST':
        cyber_risk=Cyber_Risk(request.POST)
    
        
        if cyber_risk.is_valid():
            
            subject="Cyber Risk"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("business_cyber_risk_EMAIL.html", context)    
            
           
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/business_cyber_risk_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            cyber_risk=Cyber_Risk()
            
            return redirect('success')
    return render(request, "business_cyber_risk.html", {'cyber_risk':Cyber_Risk})

def personal_home_1(request):
    if request.method=='POST':
        
        home_form=Home_P(request.POST)
        if home_form.is_valid():
            
            subject="Home Form"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("personal_home_1_EMAIL.html", context) 
                  
           
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/personal_home_1_EMAIL.html").render() 
            message.attach_alternative(email_body,"text/html")
            message.send() 
            home_form=Home_P()
           
            return redirect('success')
    return render(request, "personal_home.html", {'home_form':Home_P})

def personal_car_2(request):
    if request.method=='POST':
        
        car_form=Car_P(request.POST)
        if car_form.is_valid():
            
            subject="Car form(Personal)"
            from_email = 'pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("personal_car_2_EMAIL.html", context) 
             
            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/personal_car_2_EMAIL.html").render()
            message.attach_alternative(email_body,"text/html")
            message.send() 
            car_form=Car_P()
            
            return redirect('success')
    return render(request, "personal_car.html", {'car_form':Car_P})

def personal_travel_3(request):
    if request.method=='POST':
        
        travel_p_form=Travel_P(request.POST)
        if travel_p_form.is_valid():
            
            subject="Travel personal form"
            from_email='pinkxyro@Gmail.com'
            data = request.POST.copy()
            form=data 
            context={'form':form,'data':data}
            email_body = render_to_string("personal_travel_3_EMAIL.html", context) 
            
            
            message=EmailMultiAlternatives(subject,'hello',from_email,to=['nadchan456@Gmail.com']) 
            html_template=get_template(settings.BASE_DIR +"/templates/personal_travel_3_EMAIL.html").render() 
            message.attach_alternative(email_body,"text/html")
            message.send() 
            travel_p_form=Travel_P()
            
            return redirect('success')
    return render(request, "personal_travel.html", {'travel_p_form':Travel_P})


    
def public_liability_EMAIL_1(request):
    template_name = 'public_liability_EMAIL.html'


def successView(request):
    return render_to_response('success.html')