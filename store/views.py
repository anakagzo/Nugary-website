from django.shortcuts import render, redirect
from Moderna.secrets import TOKEN
import requests

# Create your views here.


def home(request):

    token = TOKEN
    url_product = 'http://anakagzo.pythonanywhere.com/api/products'
    url_category = 'http://anakagzo.pythonanywhere.com/api/productCategory'

    params = {'token': token,
            }
    response1 = requests.get(url_product, params)
    response2 = requests.get(url_category, params)

    if response1.status_code == 200 and response2.status_code == 200:
        products = response1.json()
        categories = response2.json()
        return render(request, 'store/index.html', 
                    {'products': products,
                     'categories': categories})
    else:
        products = []
        categories = []
        return render(request, 'store/index.html', 
                    {'products': products,
                     'categories': categories})


def get_product(request):
    #find the product from the database

    token = TOKEN
    url = 'http://anakagzo.pythonanywhere.com/api/products'
    if request.method == 'POST':
        product = request.POST['product']
        params = {'token': token,
            'name': product}
        response = requests.get(url, params)
        if response.status_code == 200:
            products = response.json()
            return render(request, 'store/get_products.html', 
                        {'products': products})
        else:
            return render(request, 'store/get_products.html', 
                        {'msg': 'product does not exist'})
    else:
        if 'cat' in request.GET:
            params = {'token': token,
                'cat': request.GET['cat']}
            response = requests.get(url, params)
            if response.status_code == 200:
                products = response.json()
                return render(request, 'store/get_products.html', 
                            {'products': products})
            else:
                return render(request, 'store/get_products.html', 
                            {'msg': 'product does not exist'})
        elif 'name' in request.GET and 'brand' in request.GET:
            params = {'token': token,
                'name': request.GET['name'],
                'brand': request.GET['brand']}
            response = requests.get(url, params)
            if response.status_code == 200:
                products = response.json()
                return render(request, 'store/get_products.html', 
                            {'products': products})
            else:
                return render(request, 'store/get_products.html', 
                            {'msg': 'product does not exist'}) 
        else:
            return redirect('home')
    

def about(request):

    return render(request, 'store/about.html')


def contact(request):

    return render(request, 'store/contact.html')


def tips(request):

    return render(request, 'store/blog.html')


def tips_details(request):

    return render(request, 'store/blog-single.html')


def login(request):

    return render(request, 'store/login.html')