from django.urls import path
from .import views

urlpatterns = [
    path('register-applicant/',views.register_applicant,name='register-applicant'),
    path('register-recruiter/',views.register_recruiter,name='register-recruiter'),
    path('login/',views.register_applicant,name='login'),
    path('logout/',views.register_applicant,name='logout')

]
