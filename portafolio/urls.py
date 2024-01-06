from core import views
from portafolio_backend.views import portafolio
from about.views import about
from blog.views import blog
from post.views import index, post_detail

from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static 

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("about/", about, name="about"),
    path("portafolio/", portafolio, name="portafolio"),
    path("contacto/", views.contacto, name="contacto"),
    path("blog/", blog, name="blog"),
    path("index/", index, name="index"),
    path("index/<int:post_id>", post_detail, name="post_detail")

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


