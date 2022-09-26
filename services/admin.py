from django.contrib import admin
from .models import Commande, Service, Portfolio, Terms

# Register your models here.

admin.site.register(Commande)
admin.site.register(Service)
admin.site.register(Portfolio)
admin.site.register(Terms)