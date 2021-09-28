from django.urls import path, include
from rest_framework.routers import DefaultRouter

from ..views.common import (ExpendViewSet)

router = DefaultRouter()
router.register(r"expend", ExpendViewSet, basename="expend")

urlpatterns = [
    path("", include(router.urls)),
]
