from dataclasses import fields
from pyexpat import model 
from .models import Appointment,Payment
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
import datetime

class BookAppointmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'

        validators = [
            UniqueTogetherValidator(
                queryset=Appointment.objects.all(),
                fields=['appointment_date', 'appointment_slot', 'doctor_id']
            )
        ]

    def validate(self, data):
        if data['appointment_date'] < datetime.date.today():
            raise serializers.ValidationError("Select a date of tomorrow or later")
        
        return data

# class modifyAppointmentSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Appointment
#         fields = '__all__'

class PaymentSerializers(serializers.ModelSerializer):
    class Meta:
        model=Payment
        fields=['id','appointment_id','card_number','account_name','cvv','expiry_date']
