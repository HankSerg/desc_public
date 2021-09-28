from django.urls import path, include

from .common import urlpatterns as common

urlpatterns = [
    path('common/', include(common)),
]
