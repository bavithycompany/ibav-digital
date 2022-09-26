from django.conf.urls.static import static
from django.urls import path
from .views import BlogHome, article_post
from BavMain.settings import MEDIA_URL, MEDIA_ROOT


urlpatterns = [
    path('', BlogHome, name="blog"),
    path('article-post/<str:slug>/', article_post, name='article'),
] + static(MEDIA_URL, document_root=MEDIA_ROOT)
