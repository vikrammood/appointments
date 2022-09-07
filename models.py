from django.db import models

# Create your models here.
class Appointment(models.Model):
    time_slot=[
        ('9','9'),
        ('12','12'),
        ('3','3')
    ]
    patient_name=models.CharField(max_length=191)
    patient_id = models.CharField(max_length=191)
    phone = models.CharField(max_length=191)
    email = models.CharField(max_length=191)
    address = models.CharField(max_length=191)
    appointment_slot =models.CharField(max_length=100,choices=time_slot,default='9' )
    appointment_date=models.DateField(auto_now_add=False,auto_now=False,blank=True)
    doctor_name =  models.CharField(max_length=191)
    doctor_id = models.CharField(max_length=191)
    booking_status=models.BooleanField(default=False)
    gender = models.CharField(max_length=191)
    symptoms = models.CharField(max_length=255)

    

class Payment(models.Model):
    appointment_id = models.ForeignKey(Appointment,default=1,on_delete=models.SET_DEFAULT)
    card_number=models.CharField(max_length=255)
    account_name=models.CharField(max_length=255)
    cvv=models.CharField(max_length=4,unique=True)
    expiry_date=models.DateField(max_length=255)
    