from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', DocumentList.as_view(), name='index'),
    path('create/', DocumentCreate.as_view(), name='create'),
    path('<int:pk>/', DocumentDetail.as_view(), name='detail'),
    path('<int:pk>/update/', DocumentUpdate.as_view(), name='update'),
    path('<int:pk>/delete/', DocumentDelete.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)