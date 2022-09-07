from django.urls import path
from .views import RegisterView, LoginView, UserView, LogoutView, bookAppointment, modifyAppointment, deleteAppointment

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('bookappointment', bookAppointment.as_view()),
    path('modifyappointment', modifyAppointment.as_view()),
    path('deleteappointment', deleteAppointment.as_view())
]
