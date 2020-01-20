from django import forms
from django.contrib.auth.models import User
from .models import Worker, Report
from django.contrib.admin.widgets import AdminDateWidget


class UserForm(forms.Form):
    password  = forms.CharField(widget=forms.PasswordInput(attrs={"name":"password", "placeholder":"أدخل كلمة المرور", "class":"form-control form-control-line"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"name":"password2", "placeholder":"أعد كتابة كلمة المرور", "class":"form-control form-control-line"}))

class UserNameForm(forms.ModelForm):
    class Meta:
        model = User
        fields  = ['username']
        widgets = {
            'username' : forms.TextInput(attrs={"name":"username", "placeholder":"أدخل أسم المستخدم", "class":"form-control form-control-line"}),
        }

class ReportForm(forms.ModelForm):
    class Meta:
        model   = Report
        fields  = ['installment', 'date_of_exp', 'date_of_paid']
        widgets = {
            'installment'  : forms.TextInput(attrs={"name":"installment", "placeholder":"القسط", "class":"form-control form-control-line"}),
            'date_of_exp'  : forms.DateInput(attrs={"name":"date_of_exp", 'type':'date', "class":"form-control form-control-line", "placeholder":"تاريخ الاستحقاق"}),
            'date_of_paid' : forms.DateInput(attrs={"name":"date_of_paid", 'type':'date', "class":"form-control form-control-line", "placeholder":"تاريخ السداد"})
        }

CHOICES  = (('ممتده', 'ممتده'),('تحويل', 'تحويل'),)
CHOICES2 = (('دفعات', 'دفعات'),('اقساط', 'اقساط'),('كاش', 'كاش'),)

class UserInformation(forms.ModelForm):
    class Meta:
        model   = Worker
        fields  = ['full_name', 'id_number', 'phone_number', 'job_type', 'getting_method', 'salary',
         'salary', 'company_name', 'company_address', 'exp_date', 'sponser', 'sponser_phone', 'calculate_method'
         , 'total_money', 'paid_money', 'unpaid_money', 'exp_need', 'commercial_exp', 'resp_user_number', 'notes','nationality']
        widgets = {
            'full_name' : forms.TextInput(attrs={"name":"full_name", "placeholder":"ادخل اسم العامل", "class":"form-control form-control-line"}),
            'id_number' : forms.TextInput(attrs={"name":"id_number", "placeholder":"الرقم المدنى", "class":"form-control form-control-line"}),
            'phone_number' : forms.TextInput(attrs={"name":"phone_number", "placeholder":"رقم تليفون العامل", "class":"form-control form-control-line"}),
            'job_type' : forms.TextInput(attrs={"name":"job_type", "placeholder":"المهنه", "class":"form-control form-control-line"}),
            'getting_method' : forms.Select(choices=CHOICES, attrs={"name":"getting_method", "class":"form-control form-control-line"}),
            'salary' : forms.NumberInput(attrs={"name":"salary", "placeholder":"الراتب", "class":"form-control form-control-line"}),
            'nationality' : forms.TextInput(attrs={"name":"nationality", "placeholder":"الجنيسة", "class":"form-control form-control-line"}),
            'company_name' : forms.TextInput(attrs={"name":"company_name", "placeholder":"اسم الشركه", "class":"form-control form-control-line"}),
            'company_address' : forms.TextInput(attrs={"name":"company_address", "placeholder":"عنوان الشركه", "class":"form-control form-control-line"}),
            'exp_date' : forms.DateInput(attrs={'type':'date', "class":"form-control form-control-line", "placeholder":"تاريخ انتهاء الاقامه"}),
            'sponser' : forms.TextInput(attrs={"name":"sponser", "placeholder":"الوسيط الضامن", "class":"form-control form-control-line"}),
            'sponser_phone' : forms.TextInput(attrs={"name":"sponser_phone", "placeholder":"رقم تليفون الضامن", "class":"form-control form-control-line"}),
            'calculate_method' : forms.Select(choices=CHOICES2, attrs={"name":"calculate_method", "class":"form-control form-control-line"}),
            'total_money' : forms.NumberInput(attrs={"name":"total_money", "placeholder":"اجمالى المبلغ", "class":"form-control form-control-line"}),
            'paid_money' : forms.NumberInput(attrs={"name":"paid_money", "placeholder":"المبلغ الواصل", "class":"form-control form-control-line"}),
            'unpaid_money' : forms.TextInput(attrs={"name":"unpaid_money", "placeholder":"الباقى", "class":"form-control form-control-line", "readonly":"readonly"}),
            'exp_need' : forms.DateInput(attrs={'type':'date', "name":"exp_need", "placeholder":"تاريخ انتهاء تقدير الاحتياج", "class":"form-control form-control-line"}),
            'commercial_exp' : forms.DateInput(attrs={'type':'date', "name":"commercial_exp", "placeholder":"تاريخ انتهاء الرخصة التجارية", "class":"form-control form-control-line"}),
            'resp_user_number' : forms.TextInput(attrs={"name":"resp_user_number", "placeholder":"رقم يوزر الشؤن", "class":"form-control form-control-line"}),
            'notes' : forms.TextInput(attrs={"name":"notes", "placeholder":"ملاحظات", "class":"form-control form-control-line"}),
        }
