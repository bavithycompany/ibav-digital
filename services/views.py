from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import context
from django.utils.html import escape
from django.utils.text import slugify

from .models import Service, Commande, Portfolio, Terms
from accounts.models import Prospect


def index(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    context["portfolio"] = Portfolio.objects.order_by('description')
    return render(request, 'index.html', context=context)


def devis(request):
    context = {}
    context["services"] = Service.objects.order_by("name")
    return render(request, 'services/devis.html', context=context)


def portfolio(request):
    context = {}
    context["portfolio"] = Portfolio.objects.all()
    context["services"] = Service.objects.order_by("name")
    return render(request, 'services/portfolio.html', context=context)


def get_page_service(request, slug):
    context = {}
    context["service"] = Service.objects.get(slug=slug)
    context["services"] = Service.objects.order_by("name")
    return render(request, 'services/service_details.html', context=context)


def commande(request):
    if request.POST:
        context = {}
        projet = escape(request.POST.get("projet"))
        username = escape(request.POST.get("name"))
        email = escape(request.POST.get("email"))
        description = escape(request.POST.get("message"))
        namecompany = escape(request.POST.get("companyName"))
        budget = escape(request.POST.get("budget"))
        tel = escape(request.POST.get("phone"))
        commande_, _ = Commande.objects.get_or_create(projet=projet, username=username, namecompany=namecompany,
                                                      budget=budget, tel=tel, email_user=email,
                                                      description=description, slug=slugify(username))
        Prospect.objects.create(username=username, email=email, telephone=tel)
        context["contacter"] = commande_
        return render(request, 'vide.html', context=context)
    return render(request, 'services/devis.html')


def terms_of_use(request):
    context = {}
    context["content"] = Terms.objects.get()
    context["services"] = Service.objects.order_by("name")
    return render(request, 'condition_of_use.html', context=context)