from django.shortcuts import render, redirect
from .models import SenderModel


def add_sender_View(request):
    if request.method == "POST":
        sender = SenderModel()
        sender.first_name = request.POST.get("first_name")
        sender.last_name = request.POST.get("last_name")
        sender.email = request.POST.get("email")
        sender.subscribe = request.POST.get("subscribe") == "True"
        sender.save()
        return redirect("/")
    else:
        return render(request, "sender/add_sender.html", {})
