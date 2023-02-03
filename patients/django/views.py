from django.shortcuts import render, redirect
from .models import Patients

def transfer_request(request):
    if request.method=='POST':
        patient_id=request.POST.get('patient_id')
        try:
            patient=Patients.objects.get(id=patient_id)
        except Patients.DoesNotExist:
            return redirect('transfer error')

        request.session['patient_id']=patient.id
        request.session['patient_name']=patient.name

        return redirect('transfer confirm')

    return redirect('transfer error')


def transfer_confirm(request):
    patient_id=request.session.get('patient_id')
    patient_name=request.session.get('patient_name')

    if patient_id is None or patient_name is None:
        return redirect('transfer error')

    context={'patient_id':patient_id, 'patient_name':patient_name}
    return render(request,'transfer_confirm.html',context)



def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patient_transfer/transfer_patient_list.html', {'patients': patients})

def index(request):
    return render(request,'index.htm')

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('patient_list')
        else:
            return render(request, 'index.html', {'error': 'Invalid login credentials'})
    return render(request, 'index.html')

from django.contrib.auth.decorators import login_required

@login_required
def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})