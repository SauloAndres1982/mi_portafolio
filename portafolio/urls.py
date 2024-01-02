from core import views
from portafolio_backend.views import portafolio
from about.views import about

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", about, name="about"),
    path("portafolio/", portafolio, name="portafolio"),
    path("contacto/", views.contacto, name="contacto")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


