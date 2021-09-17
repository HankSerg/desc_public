from django.urls import path
from chatroom.views import *

urlpatterns = [
    path('room/', Rooms.as_view()),
    path('dialog/', Dialog.as_view()),
    path('users/', AddUserRoom.as_view()),
]
