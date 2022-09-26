from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Article(models.Model):
    titre = models.CharField(max_length=150, unique=True, verbose_name='Titre')
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    image = models.ImageField(upload_to='image_article')
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(default='')

    def as_default(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titre)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.titre


class Section_post(models.Model):
    titre = models.CharField(max_length=150, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    ordre = models.IntegerField()
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images_post', blank=True, null=True)

    def __str__(self):
        return self.titre