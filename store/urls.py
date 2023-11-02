from django.urls import path
from .views import home, about, contact, tips, tips_details, get_product, \
    purchase, product_details, view_cart, update_cart

urlpatterns = [
    path('', home),
    path('home', home, name='home'),   
    path('about', about, name='about'),
    path('contact', contact, name='contact'),
    path('tips', tips, name='tips'),
    path('tips_details', tips_details, name='tips_details'),
    path('products', get_product, name='get_product'),
    path('purchase', purchase, name='purchase'),
    path('product_details', product_details, name='product_details'),
    path('view_cart', view_cart, name='view_cart'),
    path('update_cart', update_cart, name='update_cart' ),
]

