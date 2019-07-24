# sendemail/forms.py
from django import forms
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
SOME_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
genderchoices = [
('female', 'Female'),
    ('male', 'Male'),
]
TRUE_FALSE_CHOICES = (
    (True, 'Yes'),
    (False, 'No')
)


DATE_INPUT_FORMATS = ['%d-%m-%Y']
class DateInput(forms.DateInput):
    input_type = 'date'
class Travel_Form(forms.Form):
	plan_v=[('1','1'),('2','2'),('3','3')]
	region=[('regional','regional'),('global','global')]
	name_of_company = forms.CharField(required=True,label="Name of Company:",widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	address = forms.CharField(required=False,label="Address",widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	tele_no = forms.IntegerField(required=False,label="Tel No:",widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	fax_no = forms.IntegerField(required=False,label="Fax No:",widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	nature_of_business = forms.CharField(required=False,label='Nature of Business ', max_length=300 ,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	name_authorised_repre=forms.CharField(required=False,label="Name of Authorised Representative:",widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	email = forms.EmailField(required=False,label='Email', max_length=250 ,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	period_of_insuarance = forms.DateField(required=False,label='Period of Insurance',widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	name_employee_1A=forms.CharField(required=False,label="")
	nationality_1A=forms.CharField(required=False,label="")
	nric_1A=forms.CharField(required=False,label="")
	country_residence_1A=forms.CharField(required=False,label="")
	dob_1A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_1A=forms.ChoiceField(required=False,choices=plan_v)
	region_1A=forms.ChoiceField(required=False,choices=region)
	premium_1A=forms.DecimalField(required=False,label="")
	name_employee_2A=forms.CharField(required=False,label="")
	nationality_2A=forms.CharField(required=False,label="")
	nric_2A=forms.CharField(required=False,label="")
	country_residence_2A=forms.CharField(required=False,label="")
	dob_2A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_2A=forms.ChoiceField(required=False,choices=plan_v)
	region_2A=forms.ChoiceField(required=False,choices=region)
	premium_2A=forms.DecimalField(required=False,label="")
	name_employee_3A=forms.CharField(label="")
	nationality_3A=forms.CharField(required=False,label="")
	nric_3A=forms.CharField(required=False,label="")
	country_residence_3A=forms.CharField(required=False,label="")
	dob_3A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_3A=forms.ChoiceField(required=False,choices=plan_v)
	region_3A=forms.ChoiceField(required=False,choices=region)
	premium_3A=forms.DecimalField(required=False,label="")
	name_employee_4A=forms.CharField(required=False,label="")
	nationality_4A=forms.CharField(required=False,label="")
	nric_4A=forms.CharField(required=False,label="")
	country_residence_4A=forms.CharField(required=False,label="")
	dob_4A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_4A=forms.ChoiceField(required=False,choices=plan_v)
	region_4A=forms.ChoiceField(required=False,choices=region)
	premium_4A=forms.DecimalField(required=False,label="")
	name_employee_5A=forms.CharField(required=False,label="")
	nationality_5A=forms.CharField(required=False,label="")
	nric_5A=forms.CharField(required=False,label="")
	country_residence_5A=forms.CharField(required=False,label="")
	dob_5A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_5A=forms.ChoiceField(required=False,choices=plan_v)
	region_5A=forms.ChoiceField(required=False,choices=region)
	premium_5A=forms.DecimalField(required=False,label="")
	name_employee_6A=forms.CharField(required=False,label="")
	nationality_6A=forms.CharField(required=False,label="")
	nric_6A=forms.CharField(required=False,label="")
	country_residence_6A=forms.CharField(required=False,label="")
	dob_6A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_6A=forms.ChoiceField(required=False,choices=plan_v)
	region_6A=forms.ChoiceField(required=False,choices=region)
	premium_6A=forms.DecimalField(required=False,label="")
	name_employee_7A=forms.CharField(required=False,label="")
	nationality_7A=forms.CharField(required=False,label="")
	nric_7A=forms.CharField(required=False,label="")
	country_residence_7A=forms.CharField(required=False,label="")
	dob_7A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_7A=forms.ChoiceField(required=False,choices=plan_v)
	region_7A=forms.ChoiceField(choices=region)
	premium_7A=forms.DecimalField(required=False,label="")
	name_employee_8A=forms.CharField(required=False,label="")
	nationality_8A=forms.CharField(required=False,label="")
	nric_8A=forms.CharField(required=False,label="")
	country_residence_8A=forms.CharField(required=False,label="")
	dob_8A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_8A=forms.ChoiceField(required=False,choices=plan_v)
	region_8A=forms.ChoiceField(required=False,choices=region)
	premium_8A=forms.DecimalField(required=False,label="")
	name_employee_9A=forms.CharField(required=False,label="")
	nationality_9A=forms.CharField(required=False,label="")
	nric_9A=forms.CharField(required=False,label="")
	country_residence_9A=forms.CharField(required=False,label="")
	dob_9A=forms.CharField(required=False,label="",        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	plan_9A=forms.ChoiceField(required=False,choices=plan_v)
	region_9A=forms.ChoiceField(required=False,choices=region)
	premium_9A=forms.DecimalField(required=False,label="")
	total_premium_A=forms.DecimalField(required=False,label="TOTAL PREMIUM (GST not required)")
	cat_employee_1B=forms.CharField(required=False,label="")
	no_employee_1B=forms.IntegerField(required=False,label="")
	plan_1B=forms.ChoiceField(required=False,choices=plan_v)
	region_1B=forms.ChoiceField(required=False,choices=region)
	premium_1B=forms.DecimalField(required=False,label="")
	cat_employee_2B=forms.CharField(required=False,label="")
	no_employee_2B=forms.IntegerField(required=False,label="")
	plan_2B=forms.ChoiceField(required=False,choices=plan_v)
	region_2B=forms.ChoiceField(required=False,choices=region)
	premium_2B=forms.DecimalField(required=False,label="")
	cat_employee_3B=forms.CharField(required=False,label="")
	no_employee_3B=forms.IntegerField(required=False,label="")
	plan_3B=forms.ChoiceField(required=False,choices=plan_v)
	region_3B=forms.ChoiceField(required=False,choices=region)
	premium_3B=forms.DecimalField(required=False,label="")
	cat_employee_4B=forms.CharField(required=False,label="")
	no_employee_4B=forms.IntegerField(required=False,label="")
	plan_4B=forms.ChoiceField(required=False,choices=plan_v)
	region_4B=forms.ChoiceField(required=False,choices=region)
	premium_4B=forms.DecimalField(required=False,label="")
	cat_employee_5B=forms.CharField(required=False,label="")
	no_employee_5B=forms.IntegerField(required=False,label="")
	plan_5B=forms.ChoiceField(required=False,choices=plan_v)
	region_5B=forms.ChoiceField(required=False,choices=region)
	premium_5B=forms.DecimalField(required=False,label="")
	total_premium_B=forms.DecimalField(required=False,label="TOTAL PREMIUM (GST not required)")
	policy_year_C1=forms.CharField(required=False,label="")
	no_claims_C1=forms.IntegerField(required=False,label="")
	total_claim_amt_C1=forms.DecimalField(required=False,label="")
	policy_year_C2=forms.CharField(required=False,label="")
	no_claims_C2=forms.IntegerField(required=False,label="")
	total_claim_amt_C2=forms.DecimalField(required=False,label="")
	policy_year_C3=forms.CharField(required=False,label="")
	no_claims_C3=forms.IntegerField(required=False,label="")
	total_claim_amt_C3=forms.DecimalField(required=False,label="")
	other_information=forms.CharField(required=False,label="")

class Public_Liability_Form(forms.Form):
	use_risk_premise = [('dwelling','Dwelling'),('manufacturing','Manufacturing'),('shop','Shop'),('others','Others,Please specify'),('engineering','Engineering'),('office','Office'),('warehouse','Warehouse')]
	CHOICE = [('yes','yes'),('no','no')]

	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	business_registration_no = forms.IntegerField(label='Business Registration No.:',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	no_of_years_business = forms.IntegerField(label='No. of Years in Business ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	period_of_insuarance = forms.CharField(label='Period of Insurance',required=False,
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}))
	nature_of_business = forms.CharField(label='Nature of Business ', max_length=300 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

	risk_address= forms.CharField(label='Address', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	risk_postal_code=forms.IntegerField(label='Postal Number ',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	use_premise=forms.ChoiceField(label="Use of Premises",choices=use_risk_premise ,required=False,widget=forms.RadioSelect)

	annual_turn_over=forms.DecimalField(required=False)
	add_info_10C=forms.DecimalField(label="Limit of Indemnity",required=False)

	one_occurence=forms.DecimalField(required=False)

	add_info_1=forms.ChoiceField(label="a) Are any workers involved in manual works in connection withinstallation, erection, repair, maintenance, testing, demolition or construction outside Insured’s premises?",required=False,choices=CHOICE, widget=forms.RadioSelect)
	add_info_2A=forms.ChoiceField(label="b) Are any workers involved in works at height of more than 30 feet abovefloor or ground level?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_2B=forms.ChoiceField(label="If Yes, will there be any scaffolding works and/or other related activities?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_3=forms.ChoiceField(label="c) Are any workers involved in works involving explosives, dangerous or toxic chemicals, e.g. chemicals that are under the Poison Act?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_4=forms.ChoiceField(label="d) Are any workers involved in excavation works, work in manholes or tunnels etc?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_5=forms.ChoiceField(label="e) Are any workers involved in using heavy industrial machines that involve cutting, pressing, grinding etc?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_6=forms.ChoiceField(label="f) Are any workers involved in lifting or hoisting operations, especially in public areas?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_7A=forms.ChoiceField(label="g) Are any workers required to work on-board vessels?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_7B=forms.IntegerField(label="If Yes, what is the maximum no. of employees on-board any vessel any one time?",required=False)
	add_info_8=forms.ChoiceField(label="h) Will there be any diving and/or related underwater activities pertaining to your business?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_9A=forms.ChoiceField(label="i) Does the building adjoin any other premises?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_9B=forms.CharField(label="If Yes, please state its nature of business: ",required=False)
	add_info_10A=forms.ChoiceField(label="j) Is there any insurance in force covering the same exposure for the same period of insurance being proposed?",choices=CHOICE, widget=forms.RadioSelect,required=False)	
	add_info_10B=forms.CharField(label="Name of Insurer:") 	
	add_info_11=forms.ChoiceField(label="k) Has any Insurance Company ever refused your Public Liability Insurance Proposal or refused to renew your Public Liability Policy?",choices=CHOICE, widget=forms.RadioSelect,required=False)
	add_info_12=forms.ChoiceField(label="l) Has your insurance been canceled solely or in part due to a breach of premium payment warranty in the last 12 months? ",choices=CHOICE, widget=forms.RadioSelect,required=False)
	


	date_of_loss_1=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	nature_of_loss_1=forms.CharField(required=False)
	amt_claimed_1=forms.DecimalField(required=False)

	date_of_loss_2=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	nature_of_loss_2=forms.CharField(required=False)
	amt_claimed_2=forms.DecimalField(required=False)

	date_of_loss_3=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	nature_of_loss_3=forms.CharField(required=False)
	amt_claimed_3=forms.DecimalField(required=False)
	
	
	
	date_of_loss_4=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	nature_of_loss_4=forms.CharField(required=False)
	amt_claimed_4=forms.DecimalField(required=False)
	
	date_of_loss_5=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	nature_of_loss_5=forms.CharField(required=False)
	amt_claimed_5=forms.DecimalField(required=False)


	name_of_insurer=forms.CharField(label="Name of Insurer:",required=False)
	limit_of_indemnity_1_occurence=forms.DecimalField(label="Any One Occurrence:",required=False)
	limit_of_indemnity_any_occurence=forms.DecimalField(label="Any One Period:",required=False)
	annual_premium=forms.DecimalField(label="Annual Premium:",required=False)
	excess=forms.DecimalField(label="Excess:",required=False)
	expiry_date=forms.DecimalField(label="Expiry Date:",required=False)
	special_terms_conditions=forms.CharField(label="Special Terms and Conditions:",required=False)


class Working_Injury_Compensation(forms.Form):
	type_of_insuarance = [('Work Injury Compensation Insurance (WIC)', 'Work Injury Compensation Insurance (WIC)'), ('Public Liability Insurance (PL)', 'Public Liability Insurance (PL)'),]
	CHOICE = [(1,'yes'),(2,'no')]

	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	business_registration_no = forms.IntegerField(label='Business Registration No.:',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	no_of_years_business = forms.IntegerField(label='No. of Years in Business ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	period_of_insuarance = forms.CharField(label='Period of Insurance', max_length=150 ,required=False,       
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}))
	nature_of_business = forms.CharField(label='Nature of Business', max_length=150 ,required=False,      
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}))
	policy_no_WIC = forms.CharField(label='Policy No. (WIC)', max_length=150,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	policy_no_PL = forms.CharField(label='Policy No. (PL)', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	typeof_insuarance= forms.ChoiceField(label='Type of Insurance',choices=type_of_insuarance)



	admin_managers_board_vessels_no_employees=forms.IntegerField(required=False,)
	admin_personal_board_vessels_no_employees=forms.IntegerField(required=False,)
	delivery_personal_board_vessels_no_employees=forms.IntegerField(required=False,)

	admin_managers_board_vessels_wages=forms.DecimalField(required=False,)
	admin_personal_board_vessels_wages=forms.DecimalField(required=False,)
	delivery_personal_board_vessels_wages=forms.DecimalField(required=False,)


	admin_managers_board_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	admin_personal_board_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	delivery_personal_board_vessels_no_employees_NOT=forms.IntegerField(required=False,)

	admin_managers_board_vessels_wages_NOT=forms.DecimalField(required=False,)
	admin_personal_board_vessels_wages_NOT=forms.DecimalField(required=False,)
	delivery_personal_board_vessels_wages_NOT=forms.DecimalField(required=False,)


	engineers_board_vessels_no_employees=forms.IntegerField(required=False,)
	engineers_board_vessels_wages=forms.DecimalField(required=False,)
	engineers_board_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	engineers_board_vessels_wages_NOT=forms.DecimalField(required=False,)

	general_workers_board_vessels_no_employees=forms.IntegerField(required=False,)
	general_workers_vessels_wages=forms.DecimalField(required=False,)
	general_workers_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	general_workers_vessels_wages_NOT=forms.DecimalField(required=False,)

	general_workersH_board_vessels_no_employees=forms.IntegerField(required=False,)
	general_workersH_vessels_wages=forms.DecimalField(required=False,)
	general_workersH_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	general_workersH_vessels_wages_NOT=forms.DecimalField(required=False,)

	management_board_vessels_no_employees=forms.IntegerField(required=False,)
	management_vessels_wages=forms.DecimalField(required=False,)
	management_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	management_vessels_wages_NOT=forms.DecimalField(required=False,)

	management_O_board_vessels_no_employees=forms.IntegerField(required=False,)
	management_O_vessels_wages=forms.DecimalField(required=False,)
	management_O_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	management_O_vessels_wages_NOT=forms.DecimalField(required=False,)

	operations_supervisor_board_vessels_no_employees=forms.IntegerField(required=False,)
	operations_supervisor_vessels_wages=forms.DecimalField(required=False,)
	operations_supervisor_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	operations_supervisor_vessels_wages_NOT=forms.DecimalField(required=False,)

	sales_management_supervisor_board_vessels_no_employees=forms.IntegerField(required=False,)
	sales_management_supervisor_vessels_wages=forms.DecimalField(required=False,)
	sales_management_supervisor_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	sales_management_supervisor_vessels_wages_NOT=forms.DecimalField(required=False,)

	sales_personal_supervisor_board_vessels_no_employees=forms.IntegerField(required=False,)
	sales_personal_supervisor_vessels_wages=forms.DecimalField(required=False,)
	sales_personal_supervisor_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	sales_personal_supervisor_vessels_wages_NOT=forms.DecimalField(required=False,)

	technician_H_supervisor_board_vessels_no_employees=forms.IntegerField(required=False,)
	technician_H_supervisor_vessels_wages=forms.DecimalField(required=False,)
	technician_H_supervisor_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	technician_H_supervisor_vessels_wages_NOT=forms.DecimalField(required=False,)

	technician_L_supervisor_board_vessels_no_employees=forms.IntegerField(required=False,)
	technician_L_supervisor_vessels_wages=forms.DecimalField(required=False,)
	technician_L_supervisor_vessels_no_employees_NOT=forms.IntegerField(required=False,)
	technician_L_supervisor_vessels_wages_NOT=forms.DecimalField(required=False,)

	C_admin_managers_no_employees=forms.IntegerField(required=False,)
	C_admin_managers_wages=forms.DecimalField(required=False,)
	C_admin_managers_no_employees_NOT=forms.IntegerField(required=False,)
	C_admin_managers_wages_NOT=forms.DecimalField(required=False,)

	C_admin_personnel_no_employees=forms.IntegerField(required=False,)
	C_admin_personnel_wages=forms.DecimalField(required=False,)
	C_admin_personnel_no_employees_NOT=forms.IntegerField(required=False,)
	C_admin_personnel_wages_NOT=forms.DecimalField(required=False,)

	C_delivery_personnel_no_employees=forms.IntegerField(required=False,)
	C_delivery_personnel_wages=forms.DecimalField(required=False,)
	C_delivery_personnel_no_employees_NOT=forms.IntegerField(required=False,)
	C_delivery_personnel_wages_NOT=forms.DecimalField(required=False,)

	C_engineers_no_employees=forms.IntegerField(required=False,)
	C_engineers_wages=forms.DecimalField(required=False,)
	C_engineers_no_employees_NOT=forms.IntegerField(required=False,)
	C_engineers_wages_NOT=forms.DecimalField(required=False,)

	C_general_workers_no_employees=forms.IntegerField(required=False,)
	C_general_workers_wages=forms.DecimalField(required=False,)
	C_general_workers_no_employees_NOT=forms.IntegerField(required=False,)
	C_general_workers_wages_NOT=forms.DecimalField(required=False,)

	C_general_workers_H_no_employees=forms.IntegerField(required=False,)
	C_general_workers_H_wages=forms.DecimalField(required=False,)
	C_general_workers_H_no_employees_NOT=forms.IntegerField(required=False,)
	C_general_workers_H_wages_NOT=forms.DecimalField(required=False,)

	C_managers_CEO_no_employees=forms.IntegerField(required=False,)
	C_managers_CEO_wages=forms.DecimalField(required=False,)
	C_managers_CEO_no_employees_NOT=forms.IntegerField(required=False,)
	C_managers_CEO_wages_NOT=forms.DecimalField(required=False,)

	C_operation_managers_no_employees=forms.IntegerField(required=False,)
	C_operation_managers_wages=forms.DecimalField(required=False,)
	C_operation_managers_no_employees_NOT=forms.IntegerField(required=False,)
	C_operation_managers_wages_NOT=forms.DecimalField(required=False,)

	C_operation_supervisors_no_employees=forms.IntegerField(required=False,)
	C_operation_supervisors_wages=forms.DecimalField(required=False,)
	C_operation_supervisors_no_employees_NOT=forms.IntegerField(required=False,)
	C_operation_supervisors_wages_NOT=forms.DecimalField(required=False,)

	C_sales_managers_no_employees=forms.IntegerField(required=False,)
	C_sales_managers_wages=forms.DecimalField(required=False,)
	C_sales_managers_no_employees_NOT=forms.IntegerField(required=False,)
	C_sales_managers_NOT=forms.DecimalField(required=False,)

	C_sales_personnel_no_employees=forms.IntegerField(required=False,)
	C_sales_personnel_wages=forms.DecimalField(required=False,)
	C_sales_personnel_no_employees_NOT=forms.IntegerField(required=False,)
	C_sales_personnel_NOT=forms.DecimalField(required=False,)

	C_technicians_heavy_no_employees=forms.IntegerField(required=False,)
	C_technicians_heavy_wages=forms.DecimalField(required=False,)
	C_technicians_heavy_no_employees_NOT=forms.IntegerField(required=False,)
	C_technicians_heavy_NOT=forms.DecimalField(required=False,)

	C_technicians_light_no_employees=forms.IntegerField(required=False,)
	C_technicians_light_wages=forms.DecimalField(required=False,)
	C_technicians_light_no_employees_NOT=forms.IntegerField(required=False,)
	C_technicians_light_NOT=forms.DecimalField(required=False,)



	marine_related_business=forms.DecimalField(required=False,)
	non_marine_related_business=forms.DecimalField(required=False)
	limit_of_liability=forms.DecimalField(required=False)

	period_3_from_A_WIC=forms.DateField(required=False,widget=forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_A_WIC=forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}),required=False)
	period_3_no_employees_A_WIC=forms.IntegerField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	paid_claims_3_No_A_WIC=forms.IntegerField(required=False,)
	paid_claims_3_Amount_A_WIC=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_A_WIC=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_A_WIC=forms.DecimalField(required=False,)

	period_3_from_B_WIC=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_B_WIC=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_no_employees_B_WIC=forms.IntegerField(required=False,)
	paid_claims_3_No_B_WIC=forms.IntegerField(required=False,)
	paid_claims_3_Amount_B_WIC=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_B_WIC=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_B_WIC=forms.DecimalField(required=False,)

	period_3_from_C_WIC=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_C_WIC=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_no_employees_C_WIC=forms.IntegerField(required=False,)
	paid_claims_3_No_C_WIC=forms.IntegerField(required=False,)
	paid_claims_3_Amount_C_WIC=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_C_WIC=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_C_WIC=forms.DecimalField(required=False,)

	period_3_from_A_public=forms.DateField(required=False,       
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_A_public=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_no_employees_A_public=forms.IntegerField(required=False,)
	paid_claims_3_No_A_public=forms.IntegerField(required=False,)
	paid_claims_3_Amount_A_public=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_A_public=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_A_public=forms.DecimalField(required=False,)

	period_3_from_B_public=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_B_public=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_no_employees_B_public=forms.IntegerField(required=False,)
	paid_claims_3_No_B_public=forms.IntegerField(required=False,)
	paid_claims_3_Amount_B_public=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_B_public=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_B_public=forms.DecimalField(required=False,)

	period_3_from_C_public=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_to_C_public=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_3_no_employees_C_public=forms.IntegerField(required=False,)
	paid_claims_3_No_C_public=forms.IntegerField(required=False,)
	paid_claims_3_Amount_C_public=forms.DecimalField(required=False,)
	outstanding_claims_3_no_employees_C_public=forms.IntegerField(required=False,)
	outstanding_claims_3_Amount_C_public=forms.DecimalField(required=False,)

	max_no_employees=forms.IntegerField(label="What is the maximum no. of employees involved in work-on-board vessel any one time?")
	welding_hot_work_yesno=forms.ChoiceField(label="Does the work involve welding work and/or hot-work?",choices=CHOICE, widget=forms.RadioSelect,required=False,)
	work_on_board=forms.ChoiceField(label="Work-on-Board offshore oil-rigs",choices=CHOICE, widget=forms.RadioSelect,required=False,)
	sail_vessel_contract=forms.ChoiceField(label="Sail with the vessel to complete the contract/assignment",choices=CHOICE, widget=forms.RadioSelect,required=False,)

	max_no_employees_oilrigs=forms.CharField(required=False,label="") 
	max_no_employees_sailvessel=forms.CharField(required=False,label="") 

	average_duration_oilrigs=forms.CharField(required=False,label="") 
	average_duration_sailvessel=forms.CharField(required=False,label="") 

	location_offshore_oilrigs=forms.CharField(required=False,label="") 
	location_offshore_sailvessel=forms.CharField(required=False,label="") 

	frequency_oilrigs=forms.CharField(required=False,label="") 
	frequency_sailvessel=forms.CharField(required=False,label="") 

	annex=forms.CharField(required=False,label="") 


class Property_All_Risks(forms.Form):
	use_premise=[('Dwelling','Dwelling'),
	('Manufacturing','Manufacturing'),
	('Shop','Shop'),
	('Engineering','Engineering'),
	('Office','Office'),
	('Warehouse','Warehouse'),
	('Others(please specify)','Others(please specify)'),
	]
	yes_no=[('Yes','Yes'),('No','No')]
	cover_required=[('All Risks','All Risks'),('Fire & Extraneous Perils','Fire & Extraneous Perils')]
	use_premise_A=[('Brick','Brick'),('Concrete','Concrete'),('Open-Sided','Open-Sided'),('Others','Others')]
	use_premise_B=[('Concrete','Concrete'),('Zinc','Zinc'),('Tiles','Tiles'),('Others','Others')]
	use_premise_C=[('Concrete','Concrete'),('Metal','Metal'),('Wooden','Wooden'),('Others','Others')]
	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	business_registration_no = forms.IntegerField(label='Business Registration No.:',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))	
	email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))	
	period_of_insuarance = forms.CharField(label='Period of Insurance', max_length=150 ,required=False, 
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}))
	no_of_years_business = forms.IntegerField(label='No. of Years in Business ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	mortgagee=forms.CharField(label="Mortgagee (if any):",required=False,)
	nature_of_business = forms.CharField(label='Nature of Business ', max_length=300 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	risk_adress= forms.CharField(label='Address: ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	risk_postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	use_of_premise_qns1=forms.MultipleChoiceField(label="Use of Premises ",choices=use_premise , widget=forms.CheckboxSelectMultiple(),required=False,)	
	use_of_premise_qns2A=forms.ChoiceField(label="a) Walls" ,choices=use_premise_A, widget=forms.RadioSelect,required=False,)
	use_of_premise_qns2B=forms.ChoiceField(label="b) Roof" ,choices=use_premise_B, widget=forms.RadioSelect,required=False,)
	use_of_premise_qns2C=forms.ChoiceField(label="c) Building Frame" ,choices=use_premise_C, widget=forms.RadioSelect,required=False,)

	fire_alarm_yesno=forms.ChoiceField(required=False,label="1) Fire Alarm" ,choices=yes_no, widget=forms.RadioSelect)
	fire_alarm=forms.CharField(required=False,label="If Yes,where is the fire alarm connected to?")
	fire_fighting_appliance_2A=forms.ChoiceField(required=False,label="2) Fire Extinguisher" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_2B=forms.CharField(required=False,label="No:" )
	fire_fighting_appliance_3=forms.ChoiceField(required=False,label="3) Heat Detector" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_4=forms.ChoiceField(required=False,label="4) Hose Reels" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_5A=forms.ChoiceField(required=False,label="5) In-House Fire Brigade" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_5B=forms.CharField(required=False,label="If Yes, are they trained and no. of person in the team?" )
	fire_fighting_appliance_6=forms.ChoiceField(required=False,label="6) Smoke Detecto" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_7=forms.ChoiceField(required=False,label="7) Sprinkle" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_8=forms.ChoiceField(required=False,label="8) Yard Hydrant" ,choices=yes_no, widget=forms.RadioSelect)
	fire_fighting_appliance_9=forms.CharField(required=False,label="9) Protection other than the above:")
	security_system_1=forms.ChoiceField(required=False,label="1) 24-hours Watchman Services" ,choices=yes_no, widget=forms.RadioSelect)
	security_system_2A=forms.ChoiceField(required=False,label="2) Burglar Alarm System" ,choices=yes_no, widget=forms.RadioSelect)
	security_system_2B=forms.CharField(required=False,label="Name of Brand" )
	security_system_2C=forms.ChoiceField(required=False,label="Is it connected to a central monitoring station? " ,choices=yes_no, widget=forms.RadioSelect)
	security_system_3=forms.ChoiceField(required=False,label="3) Grilled Doors" ,choices=yes_no, widget=forms.RadioSelect)
	security_system_4=forms.ChoiceField(required=False,label="4) Security Checkpoint " ,choices=yes_no, widget=forms.RadioSelect)
	security_system_5=forms.ChoiceField(required=False,label="5) Surveillance Camera " ,choices=yes_no, widget=forms.RadioSelect)
	security_system_6=forms.CharField(required=False,label="6) Others, please specify: ")
	property_to_b_insured_1=forms.DecimalField(required=False,label="Building/Improvement Cost")
	property_to_b_insured_2=forms.DecimalField(required=False,label="Furniture, Fixtures & Fittings")
	property_to_b_insured_3=forms.DecimalField(required=False,label="Office & Business Equipments")
	property_to_b_insured_4A=forms.CharField(required=False,label="Stocks & Materials Consisting of: ")
	property_to_b_insured_4B=forms.DecimalField(required=False,label="")
	property_to_b_insured_5=forms.DecimalField(required=False,label="Plant & Machinery")
	property_to_b_insured_6A=forms.DecimalField(required=False,label="Loss of Rent: ")
	property_to_b_insured_6B=forms.DecimalField(required=False,label="")
	property_to_b_insured_7A=forms.DecimalField(required=False,label="Others, please specify: ")
	property_to_b_insured_7B=forms.DecimalField(required=False,label="")
	property_to_b_insured_7C=forms.DecimalField(required=False,label="Total Sum Insured")
	cover_required_qns=forms.ChoiceField(required=False,label="" ,choices=cover_required, widget=forms.RadioSelect)
	claim_exp_dol_1=forms.CharField(required=False,)
	claim_exp_dol_2=forms.CharField(required=False,)
	claim_exp_dol_3=forms.CharField(required=False,)
	claim_exp_dol_4=forms.CharField(required=False,)
	claim_exp_dol_5=forms.CharField(required=False,)
	claim_exp_nol_1=forms.CharField(required=False,)
	claim_exp_nol_2=forms.CharField(required=False,)
	claim_exp_nol_3=forms.CharField(required=False,)
	claim_exp_nol_4=forms.CharField(required=False,)
	claim_exp_nol_5=forms.CharField(required=False,)
	claim_exp_amt_1=forms.DecimalField(required=False,)
	claim_exp_amt_2=forms.DecimalField(required=False,)
	claim_exp_amt_3=forms.DecimalField(required=False,)
	claim_exp_amt_4=forms.DecimalField(required=False,)
	claim_exp_amt_5=forms.DecimalField(required=False,)
	other_info_1A=forms.ChoiceField(required=False,label="1) Are there any hazardous goods stored in the premises?" ,choices=yes_no, widget=forms.RadioSelect)
	other_info_1B=forms.CharField(required=False,label="If Yes, please state the types of hazardous goods:")
	other_info_2A=forms.ChoiceField(required=False,label="2) Is the Premises shared with others?" ,choices=yes_no, widget=forms.RadioSelect)
	other_info_2B=forms.CharField(required=False,label="If Yes, please state its Nature of Business: ")
	other_info_3A=forms.ChoiceField(required=False,label="3) Does the building adjoin any other premises? " ,choices=yes_no, widget=forms.RadioSelect)
	other_info_3B=forms.CharField(required=False,label="If Yes, please state its Nature of Business:")	
	other_info_4A=forms.ChoiceField(required=False,label="4) Is there any insurance on the same property in force for the same period of insurance being proposed? " ,choices=yes_no, widget=forms.RadioSelect)	
	other_info_4B=forms.CharField(required=False,label="Name of Insurer:" )
	other_info_4C=forms.DecimalField(required=False,label="Sum Insured:")
	other_info_5=forms.ChoiceField(required=False,label="5) Has any Insurance Company ever refused your Fire/All Risks Insurance Proposal or refused to renew your Fire/All Risks Policy?" ,choices=yes_no, widget=forms.RadioSelect)
	other_info_6=forms.ChoiceField(required=False,label="6) Has your insurance been canceled solely or in part due to a breach of premium payment warranty in the last 12 months?" ,choices=yes_no, widget=forms.RadioSelect)
	name_of_insurer=forms.CharField(required=False,label="Name of Insurer:")
	sum_insured=forms.DecimalField(required=False,label="Sum Insured:")
	annual_premium=forms.DecimalField(required=False,label="Annual Premium: ")
	date_of_expiry=forms.DateField(required=False,label="Date of Expiry: ")
	excess=forms.CharField(required=False,label="Excess: ")
	special_terms_conditions=forms.CharField(required=False,label="Special Terms and Conditions: ")







































class Directors_and_Officers(forms.Form):
	CHOICE = [('yes','yes'),('no','no')]

	policy_procedure = [('Employment application','Employment application'),('Discrimination of any kind','Discrimination of any kind'),('Intimidation of any kind','Intimidation of any kind'),('Harassment of any kind','Harassment of any kind'),
	('Compliance with statutes','Compliance with statutes'),
	('Employee disciplinary/dismissal procedures','Employee disciplinary/dismissal procedures'),

	('Redundancies','Redundancies'),
	('Early retirement','Early retirement'),
	('Occupational health and safety','Occupational health and safety'),
	('Disability','Disability')
	,('Equal Opportunity','Equal Opportunity')]

	policy_procedure_2 = [('Employment application','Employment application'),('Discrimination of any kind','Discrimination of any kind'),('Intimidation of any kind','Intimidation of any kind'),('Harassment of any kind','Harassment of any kind'),
	('Compliance with statutes','Compliance with statutes'),
	('Employee disciplinary/dismissal procedures','Employee disciplinary/dismissal procedures'),

	('Redundancies','Redundancies'),
	('Early retirement','Early retirement'),
	('Occupational health and safety','Occupational health and safety'),
	('Disability','Disability')
	,('Equal Opportunity','Equal Opportunity')]
	
	true_false=[('true','true'),('false','false')]
	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	principle_adress = forms.CharField(label='Principle Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	country_incorporation=forms.CharField(required=False,label='Country of incorporation:')
	date_incorporation=forms.CharField(required=False,label='Date of incorporation or charter:',        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))	
	qns3_A=forms.CharField(required=False,label='a) Exchanges on which Proposer/Subsidiaries/Associated companies listed/traded')	
	qns3_B=forms.CharField(required=False,label='b)Total number of authorisedcommon shares of the Proposer:')	
	qns3_C=forms.CharField(required=False,label='c) Total number of outstanding common shares of the Proposer:')	
	qns3_D=forms.CharField(required=False,label='d) Total number of common shareholders of the Proposer:')	
	qns3_E=forms.CharField(required=False,label='e) Shareholders holding more than 5% of the Proposer’s outstanding common shares:')	
	qns4_A=forms.ChoiceField(required=False,label="a) Since the latest annual or interim report, has the Proposer issued any dividend or profit warning to holders of company securities?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_B=forms.ChoiceField(required=False,label="b) Have there been any changes in the board of directors of the Proposer within the past three (3) years forreasons other thandeath or retirement?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_C=forms.ChoiceField(required=False,label="c) Has the Proposer changed outside auditors in the last three (3) years?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_D1=forms.ChoiceField(required=False,label="i. Merger with, acquisition of or consolidation with another entity whose consolidated assets exceed 10% of the Proposer’sconsolidated assets" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_D2=forms.ChoiceField(required=False,label="ii. Sale, distribution or divestiture of any assets or equity other than in the ordinary course of business in anamount exceeding25% of the Proposer’s consolidated assets?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_D3=forms.ChoiceField(required=False,label="iii. Any registration for a public offering or any private placement of debt or equity securities?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns4_E1=forms.CharField(required=False,)
	qns4_E2=forms.CharField(required=False,)
	qns4_E3=forms.CharField(required=False,)
	qns4_E4=forms.CharField(required=False,)
	qns4_E5=forms.CharField(required=False,)
	qns5_A=forms.IntegerField(required=False,label="a)Total number of employee worldwide (including full time, part time and casual):")
	qns5_B1=forms.IntegerField(required=False,label="USA/Canada:")
	qns5_B2=forms.IntegerField(required=False,label="Australia:")
	qns5_C=forms.IntegerField(required=False,label="c) How many directors and/or employees left the proposer and/or its subsidiaries in the last 12months:")
	qns5_D=forms.IntegerField(required=False,label="If yes, how many?")
	qns5_E0=forms.ChoiceField(required=False,label="e) Does the proposer and its subsidiaries publish a written human resources manual, employee handbook or management guidelines?" ,choices=CHOICE, widget=forms.RadioSelect)	
	qns5_E1=forms.MultipleChoiceField(required=False,label="",choices=policy_procedure , widget=forms.CheckboxSelectMultiple())	
	qns5_E2=forms.MultipleChoiceField(required=False,label=" Please tick the following relevant box (es) if the policy/procedure is that decisions regarding the following aresubject to the prior consideration by the proposer’s human resources department, its in-house legal department or its external lawyer",choices=policy_procedure_2 , widget=forms.CheckboxSelectMultiple())	
	qns6_A1=forms.ChoiceField(required=False,label="Any antitrust, copyright, or patent litigation?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns6_A2=forms.ChoiceField(required=False,label="Any civil, criminal or administrative proceeding alleging or investigating a violation of any securitieslaw or regulations" ,choices=CHOICE, widget=forms.RadioSelect)
	qns6_A3=forms.ChoiceField(required=False,label="Any representative actions, class actions or derivative suits?" ,choices=CHOICE, widget=forms.RadioSelect)
	qns6_B=forms.ChoiceField(required=False,label=" No claims have been made against any person(s) or entity proposed for this insurance relating to employment practices (includingwrongful termination, discrimination, intimidation or harassment)? (include loss payment and defencecosts): " ,choices=true_false, widget=forms.RadioSelect)
	qns6_c=forms.ChoiceField(required=False,label="",choices=true_false, widget=forms.RadioSelect)




class Foreign_Worker_Medical(forms.Form):
	PLAN_V=[(1,'Plan A'),(2,'Plan B'),(3,'Plan C')]
	genderchoices = [('female', 'Female'),('male', 'Male'),]

	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	business_registration_no = forms.IntegerField(label='Business Registration No.:',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	no_of_years_business = forms.IntegerField(label='No. of Years in Business ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	period_of_insuarance = forms.CharField(      
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}),label='Period of Insurance', max_length=150 ,required=False)
	nature_of_business = forms.CharField(label='Nature of Business ', max_length=300 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	plan_x =  forms.ChoiceField(required=False,label="Plan Select",choices=PLAN_V, widget=forms.RadioSelect)
	annual_premium_foreign = forms.CharField(label='Annual Premium per Foreign Worker', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	no_foreign = forms.IntegerField(label='No. of Foreign Workers       <br>             ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	total_annum_premium = forms.DecimalField(label='Total Annual Premium excluding prevailing GST (7%) ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

	foreign_worker1=forms.CharField( required=False,max_length=150)
	foreign_worker2=forms.CharField(required=False, max_length=150)
	foreign_worker3=forms.CharField(required=False, max_length=150)
	foreign_worker4=forms.CharField(required=False, max_length=150)
	foreign_worker5=forms.CharField(required=False, max_length=150)
	foreign_worker6=forms.CharField(required=False, max_length=150)
	foreign_worker7=forms.CharField(required=False, max_length=150)
	foreign_worker8=forms.CharField(required=False, max_length=150)

	gender1 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender2 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender3 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender4 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender5 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender6 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender7 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)
	gender8 =  forms.ChoiceField(required=False,choices=genderchoices, widget=forms.RadioSelect)

	dob1=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob2=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob3=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob4=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob5=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob6=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob7=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	dob8=forms.DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))

	work_permit1=forms.IntegerField(required=False,)
	work_permit2=forms.IntegerField(required=False,)
	work_permit3=forms.IntegerField(required=False,)
	work_permit4=forms.IntegerField(required=False,)
	work_permit5=forms.IntegerField(required=False,)
	work_permit6=forms.IntegerField(required=False,)
	work_permit7=forms.IntegerField(required=False,)
	work_permit8=forms.IntegerField(required=False,)

	singpass1=forms.CharField( required=False,max_length=150)
	singpass2=forms.CharField( required=False,max_length=150)
	singpass3=forms.CharField(required=False, max_length=150)
	singpass4=forms.CharField( required=False,max_length=150)
	singpass5=forms.CharField( required=False,max_length=150)
	singpass6=forms.CharField( required=False,max_length=150)
	singpass7=forms.CharField( required=False,max_length=150)
	singpass8=forms.CharField(required=False, max_length=150)


class Security_Bond(forms.Form):
	from_email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	Name = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	Name_of_Security_Bond = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	Phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

class Cyber_Risk(forms.Form):
	from_email = forms.EmailField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	Name = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'})) 
	Name_of_Cyber_Risk = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	Phone_Number = forms.CharField(required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

class Home_P(forms.Form):

	types_premise = [('Apartment', 'Apartment'),('Condominium', 'Condominium'),('Detached','Detached'),('Semi-Detached','Semi-Detached'),('Terrace','Terrace'),('HDB','HDB'),('Others:','Others:')]
	is_premise=[('Owner Occupied','Owner Occupied'),('Tenant Occupied','Tenant Occupied'),('Others','Others')]

	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	NRIC = forms.CharField(label='NRIC/FIN No.', max_length=9 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	dob = DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	contact_number = forms.IntegerField(label='Contact Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	occupation = forms.CharField(label='Occupation ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	email = forms.EmailField(label='Email', max_length=250 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))


	address_to_be_insured=forms.CharField(required=False,label='Address of Premises to be Insured:', max_length=200,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_code_to_be_insured= forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	type_of_premise=forms.ChoiceField(required=False,label="Type of Premises:",choices=types_premise, widget=forms.RadioSelect)
	mortgagee=forms.CharField(required=False,label="Mortgagee (if to be Named in the Policy):")
	name_of_landlord=forms.CharField(required=False,label="Name of Landlord (if to be Named in the Policy):")
	is_the_premise=forms.ChoiceField(required=False,label="Is the Premises: ",choices=is_premise, widget=forms.RadioSelect)

	period_of_insuarance = forms.CharField(label='Period of Insurance', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))

class Car_P(forms.Form):	
	genderchoices = [
('female', 'Female'),
    ('male', 'Male'),
]
	CHOICE = [(1,'yes'),(2,'no')]
	USAGE_V=[(1,'business'),(2,'Hire & Reward'),(3,'Private')]
	NCD_V=[(1,'First time buying a vehicle'),(2,'Have been driving others vehicle'),(3,'2nd/3rd vehicle'),(4,'Other reasons')]
	name_of_proposer = forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=True,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	NRIC = forms.CharField(label='NRIC/FIN No.', max_length=9 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	business_registration_no = forms.IntegerField(label='Business Registration No.:',required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	occupation = forms.CharField(label='Occupation', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	nature_of_business = forms.CharField(label='Nature of Business ', max_length=300 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	mailing_adress = forms.CharField(label='Mailing Address ', max_length=200 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	postal_number = forms.IntegerField(label='Postal Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	contact_number = forms.IntegerField(label='Contact Number ', required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	gender=forms.ChoiceField(choices=genderchoices)		
	email = forms.EmailField(label='Email', max_length=250 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	nationality = forms.CharField(label='Nationality', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	dob = DateField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	period_of_insuarance = forms.CharField(label='Period of Insurance', max_length=150 ,required=False,
                           widget= forms.TextInput(attrs={'class':'datepicker','autocomplete': 'off'}))
	years_of_driving_exp = forms.CharField(label='Years of Driving Experience ', max_length=150 ,required=True,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	marital_status = forms.CharField(label='Marital Status', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	west_malaysia = forms.CharField(label='How often do you drive to West Malaysia', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	date = forms.CharField(label='Date', max_length=150 ,required=False,widget=forms.TextInput(attrs={'autocomplete': 'off'}))
	total_claim_amt = forms.BooleanField(required=False,label='Total Claim ')
	name_of_proposer2=forms.CharField(label='Name of Proposer/Name of Company', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	brand_new_vehicle=forms.ChoiceField(required=False,choices=CHOICE, widget=forms.RadioSelect)
	off_peak_car=forms.ChoiceField(required=False,choices=CHOICE, widget=forms.RadioSelect)
	registration_number = forms.CharField(label='Registration Number', max_length=50 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	make_n_model = forms.CharField(label='Make and Model', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	engine_capacity = forms.CharField(label='Engine Capacity', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	type_of_body = forms.CharField(label='Type of Body', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	chasis_no = forms.CharField(label='Chasis No.', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	engine_no = forms.CharField(label='Engine No.', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	year_of_manufacture = forms.CharField(label='Year of Manufacture/ Year of Registration', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	parallel_import = forms.ChoiceField(required=False,label="Parallel Import",choices=CHOICE, widget=forms.RadioSelect)
	turbo_engine =  forms.ChoiceField(required=False,label="Turbo Engine",choices=CHOICE, widget=forms.RadioSelect)
	usage_of_vehicle =forms.ChoiceField(required=False,choices=USAGE_V, widget=forms.RadioSelect)
	estimated_market_val = forms.DecimalField(required=False,label='Estimated Market Value.',widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	finance_co = forms.CharField(label='Name of Finance Company', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	no_of_seats = forms.IntegerField(label='No. of Seats',required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	no_claim_discount = forms.CharField(label='No-Claim Discount (NCD)', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	offence_free_discount = forms.ChoiceField(required=False,label="Offence Free Discount (OFD)",choices=CHOICE, widget=forms.RadioSelect)
	ncd_protector = forms.ChoiceField(required=False,label="NCD Protector",choices=CHOICE, widget=forms.RadioSelect)
	current_vehicle_ncd_transfer = forms.CharField(label='Current Vehicle for NCD Transfer', max_length=150 ,required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	current_insurance_company = forms.CharField(label='Current Insurance Company',required=False,widget=forms.Textarea(attrs={'cols':1,'rows':1}))
	date_of_current_policy = forms.CharField(label='Date of Current Policy Expiry/Cancelation',        
                           widget= forms.TextInput(attrs={'class':'datepicker'}),required=False)
	ncd_nil =forms.ChoiceField(required=False,label="If NCD is “NIL”, please provide reasons",choices=NCD_V, widget=forms.RadioSelect)
	modification_accessories =forms.ChoiceField(required=False,label="Any Modification/Accessories",choices=CHOICE, widget=forms.RadioSelect)
	demerit_points =forms.ChoiceField(required=False,label="Been given demerit points for traffic offences?",choices=CHOICE, widget=forms.RadioSelect)
	defective_vision =forms.ChoiceField(required=False,label="Have you suffered from defective vision or hearing, heart condition,epilepsy, diabetes or any physical or mental disability or infirmity that could impair the ability to drive?",choices=CHOICE, widget=forms.RadioSelect)
	refused_motor =forms.ChoiceField(required=False,label=". Been refused motor insurance at any time or subjected to special conditions?",choices=CHOICE, widget=forms.RadioSelect)
	insuarance_termination =forms.ChoiceField(required=False,label="Do you have any insurance terminated in the last 12 months due to breach of any premium payment conditions?",choices=CHOICE, widget=forms.RadioSelect)
	medical_examination =forms.ChoiceField(required=False,label="Have you ever had been identified as unfit to drive in any Medical Examination for Driving License in the past?",choices=CHOICE, widget=forms.RadioSelect)
	yes_apply = forms.CharField(required=False,label='If any of the above answers are “Yes”, please provide details:', max_length=300 ,widget=forms.Textarea(attrs={'cols':5,'rows':5}))



	name_driver_1=forms.CharField(required=False,)
	NRIC_dirver_1=forms.CharField(required=False,)
	DOB_driver_1=forms.CharField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	gender_driver_1=forms.CharField(required=False,)
	rs_to_proposer_driver_1=forms.CharField(required=False,)
	claims_2_driver_1=forms.CharField(required=False,)
	years_exp_driver_1=forms.CharField(required=False,)
	occupation_driver_1=forms.CharField(required=False,)

	name_driver_2=forms.CharField(required=False,)
	NRIC_driver_2=forms.CharField(required=False,)
	DOB_driver_2=forms.CharField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	gender_driver_2=forms.CharField(required=False,)
	rs_to_proposer_driver_2=forms.CharField(required=False,)
	claims_2_driver_2=forms.CharField(required=False,)
	years_exp_driver_2=forms.CharField(required=False,)
	occupation_driver_2=forms.CharField(required=False,)

	name_driver_3=forms.CharField(required=False,)
	NRIC_driver_3=forms.CharField(required=False,)
	DOB_driver_3=forms.CharField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	gender_driver_3=forms.CharField(required=False,)
	rs_to_proposer_driver_3=forms.CharField(required=False,)
	claims_2_driver_3=forms.CharField(required=False,)
	years_exp_driver_3=forms.CharField(required=False,)
	occupation_driver_3=forms.CharField(required=False,)

	name_driver_4=forms.CharField(required=False,)
	NRIC_driver_4=forms.CharField(required=False,)
	DOB_driver_4=forms.CharField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	gender_driver_4=forms.CharField(required=False,)
	rs_to_proposer_driver_4=forms.CharField(required=False,)
	claims_2_driver_4=forms.CharField(required=False,)
	years_exp_driver_4=forms.CharField(required=False,)
	occupation_driver_4=forms.CharField(required=False,)

	name_driver_5=forms.CharField(required=False,)
	NRIC_driver_5=forms.CharField(required=False,)
	DOB_driver_5=forms.CharField(required=False,        
                           widget= forms.TextInput(attrs={'class':'datepicker'}))
	gender_driver_5=forms.CharField(required=False,)
	rs_to_proposer_driver_5=forms.CharField(required=False,)
	claims_2_driver_5=forms.CharField(required=False,)
	years_exp_driver_5=forms.CharField(required=False,)
	occupation_driver_5=forms.CharField(required=False,)

	detail_date_1=forms.DateField(required=False,)
	detail_claim_amt_1=forms.DecimalField(required=False,)
	detail_description_1=forms.CharField(required=False,)

	detail_date_2=forms.DateField(required=False,)
	detail_claim_amt_2=forms.DecimalField(required=False,)
	detail_description_2=forms.CharField(required=False,)
	
