from django.shortcuts import render
from .models import Article
from services.models import Service


def BlogHome(request):
    context = {}
    context["posts"] = Article.objects.filter(published=True)
    context["services"] = Service.objects.order_by('name')
    return render(request, 'blog/blog.html', context=context)


def article_post(request, slug):
    context = {}
    post = Article.objects.get(slug=slug)
    context["article"] = post
    context["services"] = Service.objects.order_by('name')
    return render(request, 'blog/article_blog.html', context=context)
