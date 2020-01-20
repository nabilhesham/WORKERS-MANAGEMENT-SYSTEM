from django.db import models
from django.urls import reverse
import datetime


# Create your models here.
GETTING_CHOICES=(
    ('ممتده', 'ممتده'),
    ('تحويل', 'تحويل'),
)

CALCULATING_METHOD=(
    ('دفعات', 'دفعات'),
    ('اقساط', 'اقساط'),
    ('كاش', 'كاش'),
)

class Worker(models.Model):
    full_name        = models.CharField(max_length=300)
    phone_number     = models.CharField(max_length=30, blank=True)
    id_number        = models.CharField(max_length=40, blank=True)
    job_type         = models.CharField(max_length=250, blank=True)
    getting_method   = models.CharField(choices=GETTING_CHOICES, max_length=12)
    salary           = models.DecimalField(max_digits=10, decimal_places=2)
    nationality      = models.CharField(max_length=150, blank=True)
    company_name     = models.CharField(max_length=300, blank=True)
    company_address  = models.CharField(max_length=500, blank=True)
    exp_date         = models.DateField()
    sponser          = models.CharField(max_length=200, blank=True)
    sponser_phone    = models.CharField(max_length=50, blank=True)
    calculate_method = models.CharField(choices=CALCULATING_METHOD, max_length=14)
    total_money      = models.DecimalField(max_digits=10, decimal_places=2)
    paid_money       = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    unpaid_money     = models.DecimalField(max_digits=10, decimal_places=2, blank=True)
    exp_need         = models.DateField(blank=True)
    commercial_exp   = models.DateField(blank=True)
    resp_user_number = models.CharField(max_length=100, blank=True)
    notes            = models.TextField(null=True, blank=True)

    expired          = models.BooleanField(default=False)
    created          = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('my_app:worker_detail', args=[self.id])

    def __str__(self):
        return self.full_name

    def save(self, *args, **kwargs):
        toDay = datetime.datetime.now().date()
        if self.exp_date < toDay:
            self.expired=True
        self.unpaid_money = self.total_money - self.paid_money
        super(Worker, self).save(*args, **kwargs)

class Report(models.Model):
    user               = models.ForeignKey(Worker, related_name="reports", on_delete=models.CASCADE)
    installment        = models.DecimalField(max_digits=10, decimal_places=2)
    date_of_exp        = models.DateField()
    date_of_paid       = models.DateField()

    def __str__(self):
        return self.user.full_name
