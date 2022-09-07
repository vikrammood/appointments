from django.urls import path
from .views import BookAppointment, PatientAppointmentDetails, DoctorAppointmentDetails, PaymentView,ModifyView , DeleteView

urlpatterns = [
    path('appointment', BookAppointment.as_view()),
    path('patientappointmentdetails/<int:pk>', PatientAppointmentDetails.as_view()),
    path('doctorappointmentdetails/<int:pk>', DoctorAppointmentDetails.as_view()),
    path('payment/',PaymentView.as_view(),name='payment'),
    path('modifyappointment', ModifyView),
    path('deleteappointment', DeleteView)
]

