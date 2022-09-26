from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils.html import escape
from .models import Prospect, Contacteur
from services.models import Service


def contact(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    return render(request, 'accounts/contact.html', context=context)


def contacter_signup(request):
    if request.POST:
        context = {}
        username = escape(request.POST.get("C_username"))
        email = escape(request.POST.get("C_email"))
        telephone = escape(request.POST.get("C_telephone"))
        message = escape(request.POST.get("C_message"))

        Contacteur.objects.create(username=username, email=email, telephone=telephone, content=message)
        Prospect.objects.create(username=username, email=email, telephone=telephone)

        return render(request, 'vide.html', context={"contacter": Contacteur.username})

    return render(request, 'accounts/contact.html')
