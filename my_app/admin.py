from django.contrib import admin
from .models import Worker, Report
# Register your models here.

@admin.register(Worker)
class adminWorker(admin.ModelAdmin):
    list_display = ['full_name', 'phone_number', 'job_type', 'company_name', 'exp_date']

@admin.register(Report)
class adminWorker(admin.ModelAdmin):
    list_display = ['user', 'installment', 'date_of_paid', 'date_of_exp']
