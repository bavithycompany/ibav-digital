from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from BavMain import settings
from services import views

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('contact/', include('accounts.urls')),
    path('devis/', views.devis, name='devis'),
    path('devis_registration/', views.commande, name='devis_registration'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('service/<str:slug>/', views.get_page_service, name='service_details'),
    path("politique-de-confidentialite/", views.terms_of_use, name='terms_of_use')
    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
