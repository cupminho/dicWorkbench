from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'standard'
urlpatterns = [
    path('', StandardFormView.as_view(), name='index'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
