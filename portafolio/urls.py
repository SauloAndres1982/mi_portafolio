from core import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("portafolio/", views.portafolio, name="portafolio"),
    path("contacto/", views.contacto, name="contacto")
]
