
from django.contrib import admin
from django.urls import path,include
from enroll import  views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('enroll.urls')),
        ]


