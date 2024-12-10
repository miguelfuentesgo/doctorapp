from django.db import models

class Patient(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    contact_number = models.DecimalField(max_length=15)
    email = models.EmailField()
    address = models.TextField()
    medical_history = models.TextField()
