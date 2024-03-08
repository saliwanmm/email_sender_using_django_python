
from django.urls import include, path
from .views import add_sender_View, show_senders_View, delete_sender_View, add_newsletter_View

urlpatterns = [
    path("add_sender", add_sender_View, name="add_sender"),
    path("senders", show_senders_View, name="senders"),
    path("delete_sender/<int:id>", delete_sender_View, name="delete_sender"),
    path("add_newsletter", add_newsletter_View, name="add_newsletter"),
]
