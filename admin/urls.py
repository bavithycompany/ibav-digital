from django.conf.urls.static import static
from django.urls import path
from .views import home_admin, admin_blog, admin_ajout_article, admin_ajout_section, admin_contacter_list, admin_ajout_image_section, admin_prospect_list, ajout_section_page
from BavMain.settings import MEDIA_URL, MEDIA_ROOT

urlpatterns = [
    path('', home_admin, name='home-admin'),
    path('blog/', admin_blog, name='admin_blog'),
    path('admin_ajout_article/', admin_ajout_article, name='admin_ajout_article'),
    path('admin_ajout_section/', admin_ajout_section, name='admin_ajout_section'),
    path('admin_contacter_list/', admin_contacter_list, name='admin_contacter_list'),
    path('admin_ajout_image_section/', admin_ajout_image_section, name='admin_ajout_image_section'),
    path('admin_prospect_list/', admin_prospect_list, name='admin_prospect_list'),
    path('ajout_section_page/', ajout_section_page, name='ajout_section_page'),

] + static(MEDIA_URL, document_root=MEDIA_ROOT)