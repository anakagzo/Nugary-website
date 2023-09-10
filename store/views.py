from django.shortcuts import render, redirect
from Moderna.secrets import TOKEN
import requests

# Create your views here.


def home2(request):

    return render(request, 'store/index.html')


def home(request):
    # get the products, product categories and health tips
    # display on the home screen
    token = TOKEN
    url_product = 'http://anakagzo.pythonanywhere.com/api/products'
    url_category = 'http://anakagzo.pythonanywhere.com/api/productCategory'
    url_healthtip = 'http://anakagzo.pythonanywhere.com/api/healthtips'

    params = {'token': token,
            }
    response1 = requests.get(url_product, params)
    response2 = requests.get(url_category, params)
    response3 = requests.get(url_healthtip, params)

    if response1.status_code == 200 and response2.status_code == 200:
        products = response1.json()
        categories = response2.json()
        if response3.status_code == 200:
            healthtips = response3.json()[0:3]

        return render(request, 'store/index.html', 
                    {'products': products,
                     'categories': categories,
                     'healthtips': healthtips})
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
        else:
            return redirect('home')


def product_details(request):
    # display a single product with the details

    token = TOKEN
    url = 'http://anakagzo.pythonanywhere.com/api/products'

    if 'name' in request.GET and 'brand' in request.GET:
        params = {'token': token, 
                  'name': request.GET['name'], 
                  'brand': request.GET['brand']}
        response = requests.get(url, params)
        if response.status_code == 200:
            product = response.json()[0]
            return render(request, 'store/product-details.html', 
                        {'product': product})
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
    #find the healthtips from the database

    token = TOKEN
    url_healthtip = 'http://anakagzo.pythonanywhere.com/api/healthtips'
    url_category = 'http://anakagzo.pythonanywhere.com/api/healthtipCategory'

    if 'cat' in request.GET:
        # filter the search based on the selected category
        params = {'token': token,
                  'cat': request.GET['cat']}
        response1 = requests.get(url_healthtip, params) 
        response2 = requests.get(url_category, params)
        if response1.status_code == 200 and response2.status_code == 200:
            healthtips = response1.json()
            categories = response2.json()
            return render(request, 'store/blog.html',
                          {'healthtips': healthtips,
                           'categories': categories})
        else:
            healthtips = []
            categories = []
            return render(request, 'store/blog.html', 
                          {'healthtips': healthtips,
                           'categories': categories})
    else: 
        # if no category was passed return all categories

        params = {'token': token}
        response1 = requests.get(url_healthtip, params)
        response2 = requests.get(url_category, params)
        if response1.status_code == 200 and response2.status_code == 200:
            healthtips = response1.json()
            categories = response2.json()
            return render(request, 'store/blog.html', 
                        {'healthtips': healthtips,
                        'categories': categories})
        else:
            healthtips = []
            categories = []
            return render(request, 'store/blog.html', 
                        {'healthtips': healthtips,
                        'categories': categories})


def tips_details(request):
    #find the healthtip from the database

    token = TOKEN
    url = 'http://anakagzo.pythonanywhere.com/api/healthtips'

    if 'title' in request.GET:
        params = {'token': token,
            'title': request.GET['title']}
        response = requests.get(url, params)
        if response.status_code == 200:
            healthtip = response.json()[0]
            return render(request, 'store/blog-single.html', 
                        {'healthtip': healthtip})
        else:
            return render(request, 'store/blog-single.html', 
                        {'msg': 'healthtip does not exist'}) 
    else:
        return redirect('home')


def purchase(request):
    # display the account details for purchase

    return render(request, 'store/purchase.html')







    