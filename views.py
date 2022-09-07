from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
from .serializers import BookAppointmentSerializers, PaymentSerializers
from .models import Appointment
from rest_framework import status
import jwt, datetime,json
import requests


class BookAppointment(APIView):
    def post(self, request):
        print(request.data['jwt'])
        data=request.data['jwt']
        payload = jwt.decode(data, 'secret', algorithms=['HS256'])
        print(type(payload))
        serializer = BookAppointmentSerializers(data=payload)
        print(serializer.is_valid())
        print(serializer.errors)
        print('yes')
        serializer.save()
        return Response({"msg":"done"})
    
class PatientAppointmentDetails(APIView):
    def get(self,_,pk=None):
        print(pk)
        appointments=Appointment.objects.filter(patient_id=pk)
        serializer=BookAppointmentSerializers(appointments,many=True)
        return Response(serializer.data)

class DoctorAppointmentDetails(APIView):
    def get(self,_,pk=None):
        appointments=Appointment.objects.filter(doctor_id=pk)
        serializer=BookAppointmentSerializers(appointments,many=True)
        return Response(serializer.data)


class PaymentView(APIView):
    def post(self,request,format=None,**kwargs):
        serializer=PaymentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)#status= status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST) 




# class modifyAppointment(APIView):
#     def post(self, request,pk=None):
#         print(request.data['jwt'])
#         data=request.data['jwt']
#         payload = jwt.decode(data, 'secret', algorithms=['HS256'])
#         print(type(payload))
#         appointments=BookAppointment.objects.filter(appointment_id=pk)
#         serializer = BookAppointmentSerializers(data=payload)
#         print(serializer.is_valid())
#         print(serializer.errors)
#         print('yes')
#         serializer.save()
#         return Response({"msg":"modification done"})



@api_view(['PUT'])
def ModifyView(request):
    if request.method == 'PUT':
          print(request.data['jwt'])
          data=request.data['jwt']
          payload = jwt.decode(data, 'secret', algorithms=['HS256'])
          print(type(payload))
          appointment_id=payload['appointment_id']
          appointment=Appointment.objects.get(id=appointment_id)
          serializer =BookAppointmentSerializers(appointment,data=payload)
          print(serializer.is_valid())
          print(serializer.errors)
          print('yes')
          serializer.save()
          return Response({"msg":"modification done"})   


@api_view(['DELETE'])
def DeleteView(request):
    if request.method == 'DELETE':
          print(request.data['jwt'])
          data=request.data['jwt']
          payload = jwt.decode(data, 'secret', algorithms=['HS256'])
          print(type(payload))
          appointment_id=payload['appointment_id']
          appointment=Appointment.objects.get(id=appointment_id)
          appointment.delete()
          return Response({"msg":"deleted"})             