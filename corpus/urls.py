from django.urls import path
from .views import *

from django.conf import settings
from django.conf.urls.static import static

app_name = 'corpus'
urlpatterns = [
    path('', DocumentList.as_view(), name='index'),
    path('<int:pk>/', DocumentDetail.as_view(), name='detail'),
    path('create/', DocumentCreate.as_view(), name='create'),
    path('update/<int:pk>/', DocumentUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', DocumentDelete.as_view(), name='delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
