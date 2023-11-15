"""gestion_santé URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from santé import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home,name='home'),
    path('about/', views.About, name='about'),
    path('contact/', views.Contact, name='contact'),
    path('admin_login/', views.Login, name='admin_login'),
    path('logout/', views.Logout_admin, name='logout_admin'),
    path('index/', views.Index, name='dashboard'),
    path('view_doctor/', views.view_doctor, name='view_doctor'),
    path('delete_doctor(?P<int:pid>)/', views.Delete_Doctor, name='delete_doctor'),
    path('add_doctor/', views.AddDoctor, name='add_doctor'),
    path('view_patient/', views.view_patient, name='view_patient'),
    path('delete_patient(?P<int:pid>)/', views.Delete_Patient, name='delete_patient'),
    path('add_patient/', views.AddPatient, name='add_patient'),
    path('view_appointment/', views.view_appointment, name='view_appointment'),
    path('delete_appointment(?P<int:pid>)/', views.Delete_Appointment, name='delete_appointment'),
    path('add_appointment/', views.AddAppointment, name='add_appointment'),
]
