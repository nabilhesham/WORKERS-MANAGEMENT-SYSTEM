from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Worker, Report
from .forms import UserForm, UserInformation, ReportForm, UserNameForm
from django.db.models import Q
from django.contrib.auth.models import User
from django.template.loader import render_to_string
import os
from django.utils import timezone
# Create your views here.

def login(request):
    if request.user.is_authenticated:
        return redirect('my_app:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username:
            try:
                user = auth.authenticate(username=username, password=password)
                if user is not None:
                    auth.login(request, user)
                    return redirect('my_app:dashboard')
                else:
                    from django.contrib import messages
                    messages.error(request, 'خطأ فى اسم المستخدم او كلمه المرور')
                    # return render(request, 'Login.html')

            except Exception as e:
                print(e)
        else:
            print("Null Value")
    return render(request, 'Login.html')

@login_required
def logout(request):
    auth.logout(request)
    return redirect('my_app:login')

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UserNameForm(instance=request.user, data=request.POST)
        password_form = UserForm(data=request.POST)
        if password_form.is_valid():
            data = password_form.cleaned_data
            if data['password'] == data['password2']:
                user = User.objects.get(id=2)
                user.set_password(data['password'])
                user.save()
                return redirect('my_app:dashboard')
            else:
                err = "كلمه السر غير متطابقه"
                return render(request, "profile.html", {'form' : form, 'err' : err})
            return redirect('my_app:dashboard')
        elif user_form.is_valid():
            data = user_form.cleaned_data
            user = User.objects.get(id=2)
            user.username = data['username']
            user.save()
            return redirect('my_app:profile')
        else:
            print("not vaild")
    user_form = UserNameForm(instance=request.user)
    password_form = UserForm()
    return render(request, "profile.html", {'user_form' : user_form, 'password_form' : password_form})

@login_required
def dashboard(request):
    workers = Worker.objects.filter(expired=False).order_by('created')[:7]
    all     = Worker.objects.all()
    ended   = Worker.objects.filter(expired=True).order_by('created')[:7]
    companies = []
    for x in all:
        companies.append(x.company_name)

    context = {
        'workers'   : workers,
        'companies' : companies,
        'ended'     : ended,
    }
    return render(request, 'dashboard.html',context)

@login_required
def worker_list(request, query=None, company=None):
    result=""
    query = request.GET.get('query')
    if query:
        queryset = Q(full_name__icontains=query) | Q(id_number__icontains=query) | Q(company_name__icontains=query) | Q(job_type__icontains=query) | Q(sponser__icontains=query)
        result = Worker.objects.filter(queryset).distinct()
        context = {'workers' : result, 'query' : query}
        return render(request, 'clients-table.html',context)

    elif company:
        workers = Worker.objects.filter(company_name=company)
        return render(request, 'clients-table.html',{'workers' : workers, 'company' : company})

    result = Worker.objects.filter(expired=False)
    return render(request, 'clients-table.html',{'workers' : result})

@login_required
def worker_ended(request):
    workers = Worker.objects.filter(expired=True)
    return render(request, "ended.html", {'workers' : workers})

@login_required
def worker_detail(request, id):
    worker = get_object_or_404(Worker, id=id)
    if request.method == 'POST':
        form  = UserInformation(instance=worker, data=request.POST)
        form2 = ReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('my_app:worker_list')
        if form2.is_valid():
            cd = form2.cleaned_data
            w = Worker.objects.get(id=id)
            Report.objects.create(user=w, installment=cd['installment'], date_of_exp=cd['date_of_exp'], date_of_paid=cd['date_of_paid'])
            return redirect('my_app:worker_list')
    form   = UserInformation(instance=worker)
    form2  = ReportForm()
    return render(request, 'Details.html',{'worker' : worker, 'form' : form, 'form2' : form2})

@login_required
def company_list(request):
    companies = []
    for x in Worker.objects.all():
        if x.company_name not in companies:
            companies.append(x.company_name)
    return render(request, 'Companies-table.html',{'companies' : companies})

@login_required
def add_worker(request):
    if request.method == 'POST':
        form = UserInformation(request.POST)
        if form.is_valid():
            form.save()
    form = UserInformation()
    return render(request, 'add.html', {'form' : form})

@login_required
def delete_worker(request, id):
    try:
        worker = Worker.objects.get(id=id)
        worker.delete()
    except Exception as e:
        print(e)
    return redirect('my_app:worker_list')

@login_required
def addToExpire_worker(request, id):
    try:
        worker = Worker.objects.get(id=id)
        worker.expired = True
        worker.save()
    except Exception as e:
        print(e)
    return redirect('my_app:worker_list')

@login_required
def reports(request):
    if request.method == 'POST':
        if id:
            i = request.POST.get('installment')
            e = request.POST.get('date_of_exp')
            p = request.POST.get('date_of_paid')
            id = request.POST.get('id')
            u = Worker.objects.get(id=id)
            Report.objects.create(user=u, date_of_exp=e, installment=i, date_of_paid=p)
            return redirect('my_app:worker_detail', id=id)
    all = Report.objects.all()
    return render(request, 'reports.html',{'reports' : all})

@login_required
def print_report(request, id):
    tz = timezone.localtime(timezone.now())
    toDay = tz.date()
    worker  = Worker.objects.get(id=id)
    context = {
        'worker' : worker,
        'toDay'  : toDay,
    }
    return render(request, "Export.html", context)
