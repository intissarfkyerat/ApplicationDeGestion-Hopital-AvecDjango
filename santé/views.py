from django.shortcuts import redirect
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Doctor, Patient, Appoinment
from .utils import get_plot
import seaborn as sns

def About(request):
    return render(request,'about.html')


def Home(request):
    return render(request,'home.html')

def Contact(request):
    return render(request, 'contact.html')

def Index(request):
    if not request.user.is_staff:
       return redirect("login")
    doctors = Doctor.objects.all()
    patient = Patient.objects.all()
    appointment = Appoinment.objects.all()
    d = 0
    p = 0
    a = 0
    y = ['Doctors', 'Patients', 'Appointments']
    for i in doctors:
       d += 1
    for i in patient:
       p += 1
    for i in appointment:
       a += 1
    x = [d, p, a]
    c = sns.color_palette('pastel')[0:3]
    au = '%.0f%%'
    chart = get_plot(x, y, c, au)
    d1 = {'d': d, 'p': p, 'a': a, 'chart': chart}
    return render(request, "index.html", d1)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['aname']
        p = request.POST['pswd']
        user = authenticate(username=u,password=p)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
            else:
                error = "yes"
        except:
            error = "yes"
    d={"error": error}
    return render(request, 'login.html',d)


def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('home')

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doctor.objects .all()
    d = {'doc': doc}
    return render(request,'view_doctor.html',d)


def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doctor.objects .get(id = pid)
    doctor.delete()
    return redirect('view_doctor')


def AddDoctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        sp = request.POST['special']
        try:
            Doctor.objects.create(Name=n, mobile=m, special=sp)
            error = "no"
        except:
            error = "yes"
    d={"error": error}
    return render(request, 'add_doctor.html',d)

def view_patient(request):
    if not request.user.is_staff:
        return redirect('login')
    pat = Patient.objects.all()
    d = {'pat': pat}
    return render(request,'view_patient.html',d)


def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Patient.objects .get(id = pid)
    patient.delete()
    return redirect('view_patient')


def AddPatient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    if request.method == "POST":
        n = request.POST['name']
        m = request.POST['mobile']
        g = request.POST['gender']
        ad = request.POST['address']
        try:
            Patient.objects.create(name=n, mobile=m, gender=g, address=ad)
            error = "no"
        except:
            error = "yes"
    d={"error": error}
    return render(request, 'add_patient.html',d)


def view_appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    apo = Appoinment.objects.all()
    d = {'apo': apo}
    return render(request,'view_appointment.html',d)


def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    appointment = Appoinment.objects.get(id = pid)
    appointment.delete()
    return redirect('view_appointment')


def AddAppointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doctor.objects.all()
    patient1 = Patient.objects.all()

    if request.method == "POST":
        nd = request.POST['dname']
        np = request.POST['pname']
        d = request.POST['date']
        t = request.POST['time']
        doctor = Doctor.objects.filter(Name=nd).first()
        patient = Patient.objects.filter(name=np).first()

        try:
            Appoinment.objects.create(Doctor=doctor, Patient=patient, date=d, time=t)
            error = "no"
        except:
            error = "yes"

    d = {"doctor": doctor1, "patient": patient1, "error": error}
    return render(request, 'add_appointment.html', d)