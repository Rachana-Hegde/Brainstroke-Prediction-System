from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    date = models.DateTimeField()
    department = models.CharField(max_length=100)
    doctor = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class StrokePrediction(models.Model):
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10)
    hypertension = models.BooleanField()
    heart_disease = models.BooleanField()
    work_type = models.CharField(max_length=30)
    avg_glucose_level = models.FloatField()
    bmi = models.FloatField()
    smoking_status = models.CharField(max_length=30)
    prediction_result = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.gender}, Age {self.age} - {self.prediction_result}"
