from django.urls import path
from .views import contact, contacter_signup

urlpatterns = [
    path('', contact, name='contact'),
    path('contact/', contacter_signup, name='contacter'),
]