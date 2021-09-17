from django.conf.urls import url
from . import views
from .views import  AutoListView

urlpatterns = [
    # url(r'^$', views.auto_list, name='auto_list'),
    url(r'^$', AutoListView.as_view(), name='auto_list'),
]