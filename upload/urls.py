from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import UploadViewset


router = DefaultRouter()
router.register(r'uploads', UploadViewset)

urlpatterns = [
    path('', include(router.urls)),
]
