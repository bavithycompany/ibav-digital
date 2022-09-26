from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.html import escape
from accounts.models import Prospect, Contacteur
from blog.models import Article, Section_post, Image_post
from services.models import Cat_service, Service, Portfolio, Commande


# Views for users accounts

def home_admin(request):
    render(request, 'admin/home.html')


def admin_prospect_list(request):
    propects = Prospect.objects.order_name('name')
    return render(request, 'admin/list_prospect.html', context={"prospects": propects})


def admin_contacter_list(request):
    contacter = Contacteur.objects.order_name('name')
    return render(request, 'admin/list_prospect.html', context={"contacter": contacter})


# Views for blog

def admin_blog(request):
    # Recupere les articles publie et non publie
    context = {}
    context["article_publie"] = Article.objects.filter(published=True)
    context["article_non_publie"] = Article.objects.filter(published=False)
    render(request, 'admin/blog.html', context=context)


# view qui redirige vers la page d'edition d'une section

def ajout_section_page(request, slug):
    article = Article.objects.get(slug=slug)
    render(request, 'admin/ajout_section.html')


def admin_ajout_image_section(request, slug):
    if request.POST:
        image = request.POST.get("image")
        image = Image_post.objects.create(image=image)
        if image:
            section = Section_post.objects.get(slug=slug)
            section.image.add(image)
            section.save()
            return redirect(reverse("ajout_section"))
    return render(request, 'surplace')


def admin_ajout_section(request, slug):
    if request.POST:
        titre = escape(request.POST.get("titre_section"))
        content = escape(request.POST.get("content_section"))
        image = request.post.get("image_section")
        ordre = escape(request.POST.get("ordre_section"))

        section = Section_post.objects.create(titre=titre, content=content, image=image, ordre=ordre)
        article = Article.objects.get(slug=slug)
        if section:
            article.sections.add(request, section)
            article.save()
            return redirect(reverse("ajout_section"))
    return render(request, 'admin/ajout_section_page.html')


def admin_ajout_article(request):
    if request.POST:
        titre = escape(request.post.get("titre_article"))
        image = request.post.get("image_article")
        Article.objects.create(titre=titre, image=image)
        return render(request, 'admin/blog.html')
    return render(request, 'admin/blog.html')


def admin_delete_article(request, slug):
    article = Article.objects.get(slug=slug)
    article.delete()
    return render(request, 'admin/blog.html')


# views pour l'administration des services

# fonction pour les categories
#######################################################

def ajout_cat(request):
    if request.POST:
        nom = escape(request.POST.get("nom_cat"))
        image = escape(request.POST.get("image_cat"))
        description = escape(request.POST.get("description_cat"))
        Cat_service.objects.create(name=nom, description=description, image=image)
        return render(request, 'admin/ajout_cat.html')
    return render(request, 'admin/ajout_cat.html')


def delete_cat(request, slug):
    cat = Cat_service.objects.get(slug=slug)
    cat.delete()
    return render(request, 'admin/categorie.html')


def modif_cat(request, slug):
    if request.POST:
        n_nom = escape(request.POST.get("n_nom"))
        n_image = escape(request.POST.get("n_image"))
        n_description = escape(request.POST.get("n_description"))

        cat = Cat_service.objects.get(slug=slug)
        cat.delete()

        Cat_service.objects.create(name=n_nom, image=n_image, description=n_description)
        return render(request, 'admin/admin/categorie.html')


# fonction pour les services
##################################################################################
##################################################################################

def ajout_service(request):
    if request.POST:
        nom = escape(request.POST.get("nom_ser"))
        image = escape(request.POST.get("image_ser"))
        description = escape(request.POST.get("description_ser"))
        Service.objects.create(name=nom, description=description, image=image)
        return render(request, 'admin/ajout_ser.html')
    return render(request, 'admin/ajout_ser.html')


def delete_service(request, slug):
    service = Service.objects.get(slug=slug)
    service.delete()
    return render(request, 'admin/service.html')


def modif_service(request, slug):
    if request.POST:
        n_nom = escape(request.POST.get("n_nom"))
        n_image = escape(request.POST.get("n_image"))
        n_description = escape(request.POST.get("n_description"))

        service = Service.objects.get(slug=slug)
        service.delete()

        Service.objects.create(name=n_nom, image=n_image, description=n_description)
        return render(request, 'admin/admin/service.html')


# fonction pour le portfolio
#########################################################################
#########################################################################

def ajout_portfolio(request):
    if request.POST:
        nom = escape(request.POST.get("nom_portfolio"))
        image = escape(request.POST.get("image_portfolio"))
        description = escape(request.POST.get("description_portfolio"))
        Portfolio.objects.create(name=nom, description=description, image=image)
        return render(request, 'admin/ajout_portfolio.html')
    return render(request, 'admin/ajout_portfolio.html')


def delete_portfolio(request, slug):
    portfolio = Portfolio.objects.get(slug=slug)
    portfolio.delete()
    return render(request, 'admin/portfolio.html')


def modif_portfolio(request, slug):
    if request.POST:
        n_nom = escape(request.POST.get("n_nom"))
        n_image = escape(request.POST.get("n_image"))
        n_description = escape(request.POST.get("n_description"))

        portfolio = Portfolio.objects.get(slug=slug)
        portfolio.delete()

        Portfolio.objects.create(name=n_nom, image=n_image, description=n_description)
        return render(request, 'admin/portfolio.html')


# Affiche les commandes

def affiche_commande(request):
    commande = Commande.objects.all()
    return render(request, 'admin/commande.html', context={"commandes": commande})