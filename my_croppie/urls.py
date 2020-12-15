from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [
    path('upload', views.upload, name='upload'),
    path('images/<int:image_id>', views.detail, name='detail'),
    path('', views.index, name='index'), \
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
              + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
