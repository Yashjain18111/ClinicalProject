from django.db import models

# Create your models here.
class Patient(models.Model):
    lastname = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class ClinicalData(models.Model):
    COMPONENT_NAMES = [('hw','Height/Weight'),('bp','Blood Pressure'),('heartrate','Heart Rate')]
    componentName = models.CharField(choices=COMPONENT_NAMES,max_length=20)
    componentValue = models.CharField(max_length=20)
    measuredDateTime = models.DateTimeField(auto_now_add=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

