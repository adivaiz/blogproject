
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("blog.urls")) # so we dont need word to load
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

#the static tell django to show the media