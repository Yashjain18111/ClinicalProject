from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from clinicalsApp.models import Patient, ClinicalData
from django.urls import reverse_lazy
from clinicalsApp.forms import ClinicalDataForm
# Create your views here.


class PatientListView(ListView):
    model = Patient
class PatientCreateView(CreateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname', 'lastname','age')

class PatientUpdateView(UpdateView):
    model = Patient
    success_url = reverse_lazy('index')
    fields = ('firstname', 'lastname','age')

class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')

def addData(request, **kwargs):
    form = ClinicalDataForm()
    patient = Patient.objects.get(id=kwargs['pk'])
    if request.method == 'POST':
        form = ClinicalDataForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'clinicalsApp/clinicaldata_form.html',{'form':form, 'patient': patient})


def analyze(request,**kwargs):
    data = ClinicalData.objects.filter(patient_id=kwargs['pk'])
    responseData = []
    for eachentry in data:
        if eachentry.componentName == 'hw':
            heightAndWeight=eachentry.componentValue.split('/')
            if len(heightAndWeight)>1:
                feetToMetres = float(heightAndWeight[0]) * 0.4536
                BMI = float(heightAndWeight[1]) / (feetToMetres * feetToMetres)
                bmientry =ClinicalData()
                bmientry.componetName='BMI'
                bmientry.componentValue=BMI
                responseData.append(bmientry)

        responseData.append(eachentry)




    return render(request,'clinicalsApp/generateReport.html',{'data':responseData})