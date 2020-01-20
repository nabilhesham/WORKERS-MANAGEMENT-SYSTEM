from django.urls import path
from . import views

app_name="my_app"

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('workers/', views.worker_list, name="worker_list"),
    path('expired/', views.worker_ended, name="worker_ended"),
    path('workers/', views.worker_list, name="search"),
    path('workers/<str:company>/', views.worker_list, name="company"),
    path('detail/<int:id>', views.worker_detail, name="worker_detail"),
    path('print/<int:id>', views.print_report, name="print_report"),
    path('add/', views.add_worker, name="add_worker"),
    path('delete/<int:id>', views.delete_worker, name="delete_worker"),
    path('addtoexpire/<int:id>', views.addToExpire_worker, name="addToExpire_worker"),
    path('companies/', views.company_list, name="company_list"),
    path('reports/', views.reports, name="reports"),
    path('profile/', views.profile, name="profile"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
]
