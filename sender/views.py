from django.shortcuts import render, redirect
from .models import SenderModel

from django.core.mail import send_mail
from django.conf import settings

# This function allows any user to subscribe on our newsletter
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

# This function allows you to retrieve all users who have subscribed to the newsletter
def show_senders_View(request):
    senders = SenderModel.objects.all()
    return render(request, "sender/all_senders.html", {
        "senders": senders,
    })
    

# This function aalows you delete any subscriber from the database
def delete_sender_View(request, id):
    sender = SenderModel.objects.get(id=id)
    sender.delete()
    return redirect("/")

# This function extracts from our database all subscribers who have given their consent to automatic mailing of messages
def add_newsletter_View(request):
    subscribers = SenderModel.objects.filter(subscribe=True)
    emails = []
    for subscriber in subscribers:
        if subscriber.subscribe == True:
            emails.append(subscriber.email)
    if request.method == "POST":
        name = request.POST["name"]
        message = request.POST["message"]
        send_mail(
            name,#title
            message,#message
            "settings.EMAIL_HOST_USER",
            emails,
            fail_silently=False
        )
    return render(request, "sender/add_newsletter.html", {})
