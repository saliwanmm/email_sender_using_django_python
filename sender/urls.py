
from django.urls import include, path
from .views import add_sender_View

urlpatterns = [
    path("add_sender", add_sender_View, name="add_sender"),
]
