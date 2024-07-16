# p1/urls.py

from django.contrib import admin
from django.urls import path
from a1.views import currDate, afterDate, beforeDate  # Import specific views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('curr/', currDate),
    path('after/', afterDate),
    path('before/', beforeDate),
]
