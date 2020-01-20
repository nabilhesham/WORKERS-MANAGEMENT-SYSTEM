# Generated by Django 2.2.4 on 2019-12-18 17:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=300)),
                ('phone_number', models.IntegerField()),
                ('job_type', models.CharField(max_length=250)),
                ('getting_method', models.CharField(choices=[('Distinct', 'Distinct'), ('Transaction', 'Transaction')], max_length=12)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('nationality', models.CharField(max_length=150)),
                ('company_name', models.CharField(max_length=300)),
                ('company_number', models.IntegerField()),
                ('company_address', models.CharField(max_length=500)),
                ('exp_date', models.DateField()),
                ('sponser', models.CharField(max_length=200)),
                ('sponser_phone', models.CharField(max_length=50)),
                ('calculate_method', models.CharField(choices=[('EXCRETION', 'EXCRETION'), ('INSTALLMENTS', 'INSTALLMENTS'), ('CASH', 'CASH')], max_length=14)),
                ('total_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unpaid_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('exp_need', models.DateField()),
                ('commercial_exp', models.DateField()),
                ('resp_user_number', models.CharField(max_length=100)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('no_of_installment', models.IntegerField()),
                ('paid_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unpaid_money', models.DecimalField(decimal_places=2, max_digits=10)),
                ('installment', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_of_exp', models.DateField()),
                ('date_of_paid', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.Worker')),
            ],
        ),
    ]