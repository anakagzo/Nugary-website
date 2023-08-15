from django.urls import path
from .views import home, about, contact, tips, tips_details, login, get_product

urlpatterns = [
    path('', home),
    path('home', home, name='home'),   
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('tips', tips, name='tips'),
    path('login', login, name='login'),
    path('tips_details', tips_details, name='tips_details'),
    path('products', get_product, name='get_product'),
]

