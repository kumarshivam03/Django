from django.contrib import admin
from django.urls import path
from a2.views import showlist
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('showlist/', showlist),
]

