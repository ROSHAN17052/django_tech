from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path("",views.Home,name="Home"),
   path("service/",views.Service,name="service"),
   path("blog/",views.Blog,name="blog"),
   path("about/", views.About, name="about"),

   path("contact/", views.Contact, name="contact")
]
