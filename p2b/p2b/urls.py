from django.contrib import admin
from django.urls import path
from a2b.views import home, studentlist,courselist,register,enrolledStudents 
urlpatterns = [
    path('secretadmin/', admin.site.urls), 
    path('',home),
    path('home/',home),
    path('studentlist/',studentlist), 
    path('courselist/',courselist), 
    path('register/',register), 
    path('enrolledlist/',enrolledStudents),
]

