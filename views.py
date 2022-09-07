from ast import Delete
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import User
import jwt, datetime


# Create your views here.
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        return response


class UserView(APIView):
    
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated User')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        
        except jwt.ExpiredSignatureError :
            raise AuthenticationFailed('Unauthenticated User')
        
        #user = User.objects.filter(id = payload['id']).first()
        #serializer = UserSerializer(user)
        k = payload['id']
        r = requests.get('http://127.0.0.1:8004/api/patientappointmentdetails/%d' % k)
        print('yes')
        return Response(r.json())


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

class bookAppointment(APIView):
    def post(self, request):
          token = request.COOKIES.get('jwt')

          if not token:
               raise AuthenticationFailed('Unauthenticated!')

          try:
               r= jwt.decode(token, 'secret', algorithms=['HS256'])
       
          except jwt.ExpiredSignatureError:
               raise AuthenticationFailed('Unauthenticated!')

          payloadA ={
            
            
            'doctor_id': request.data['doctor_id'],
            'doctor_name':request.data['doctor_name'],
            'patient_name':request.data['patient_name'],
            'patient_id': r['id'],
            'email':request.data['email'],
            'phone':request.data['phone'],
            'address':request.data['address'],
            'gender':request.data['gender'],
            'symptoms':request.data['symptoms'],
            'appointment_slot':request.data['appointment_slot'],
            'appointment_date':request.data['appointment_date'],
            'booking_status':request.data['booking_status'],
        }
 

          tokenA=jwt.encode(payloadA,'secret',algorithm='HS256')

          response=Response()
          response.data={
            "jwt":tokenA
          }
          response=requests.post("http://127.0.0.1:8004/api/appointment",data=response.data)             
          return Response(response)

     

class modifyAppointment(APIView):
    def post(self, request):
          token = request.COOKIES.get('jwt')

          if not token:
               raise AuthenticationFailed('Unauthenticated!')

          try:
               r= jwt.decode(token, 'secret', algorithms=['HS256'])
       
          except jwt.ExpiredSignatureError:
               raise AuthenticationFailed('Unauthenticated!')

          payloadB ={
            
            'appointment_id': request.data['appointment_id'],
            'doctor_id': request.data['doctor_id'],
            'doctor_name':request.data['doctor_name'],
            'patient_name':request.data['patient_name'],
            'patient_id': r['id'],
            'email':request.data['email'],
            'phone':request.data['phone'],
            'address':request.data['address'],
            'gender':request.data['gender'],
            'symptoms':request.data['symptoms'],
            'appointment_slot':request.data['appointment_slot'],
            'appointment_date':request.data['appointment_date'],
            'booking_status':request.data['booking_status'],
        }
 

          tokenA=jwt.encode(payloadB,'secret',algorithm='HS256')

          response=Response()
          response.data={
            "jwt":tokenA
          }
          response=requests.put("http://127.0.0.1:8004/api/modifyappointment",data=response.data)             
          return Response(response)          


class deleteAppointment(APIView): 
    def post(self, request):
          token = request.COOKIES.get('jwt')

          if not token:
               raise AuthenticationFailed('Unauthenticated!')

          try:
               r= jwt.decode(token, 'secret', algorithms=['HS256'])
       
          except jwt.ExpiredSignatureError:
               raise AuthenticationFailed('Unauthenticated!')

          payloadB ={
            
            'appointment_id': request.data['appointment_id'],
            
        }
 

          tokenA=jwt.encode(payloadB,'secret',algorithm='HS256')

          response=Response()
          response.data={
            "jwt":tokenA
          }
          response=requests.delete("http://127.0.0.1:8004/api/deleteappointment",data=response.data)             
          return Response(response) 
