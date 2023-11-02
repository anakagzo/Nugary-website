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
    url_product = 'https://admin.nugarypharmacy.com/api/products'
    url_category = 'https://admin.nugarypharmacy.com/api/productCategory'
    url_healthtip = 'https://admin.nugarypharmacy.com/api/healthtips'

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
    url = 'https://admin.nugarypharmacy.com/api/products'
    if request.method == 'POST':
        product = request.POST['product']
        params = {'token': token,
            'name': product}
        response = requests.get(url, params)
        if response.status_code == 200:
            products = response.json()
            if 'total_products' in request.session:
                count = request.session['total_products']
            else:
                count = ''   
            return render(request, 'store/get_products.html', 
                        {'products': products, 'count': count})
        else:
            return render(request, 'store/get_products.html', 
                        {'msg': 'product does not exist'})
    else:
        if 'cat' in request.GET:
            category = request.GET['cat'] 
            params = {'token': token,
                'cat': category}
            response = requests.get(url, params)
            if response.status_code == 200:
                products = response.json()
                if 'total_products' in request.session:
                    count = request.session['total_products']
                else:
                    count = ''   
                return render(request, 'store/get_products.html', 
                            {'products': products, 'category': category,
                              'count': count})
            else:
                return render(request, 'store/get_products.html', 
                            {'msg': 'product does not exist'})
        else:
            return redirect('home')


def product_details(request):
    # display a single product with the details

    token = TOKEN
    url = 'https://admin.nugarypharmacy.com/api/products'
    #request.session['total_products'] = None
    if 'name' in request.GET and 'brand' in request.GET:
        
        params = {'token': token, 
                  'name': request.GET['name'], 
                  'brand': request.GET['brand']}
        response = requests.get(url, params)
        if response.status_code == 200:
            product = response.json()[0]
            # get the total number of products in the cart
            if 'total_products' in request.session:
                count = request.session['total_products']
            else:
                count = ''    
            return render(request, 'store/product-details.html', 
                        {'product': product, 'count': count})
        else:
            return render(request, 'store/get_products.html', 
                        {'msg': 'product does not exist'}) 
    else:
        return redirect('home')   
     

def add_to_cart(request):
    # add product to cart

    return render(request, 'store/view_cart.html')


def about(request):

    return render(request, 'store/about.html')


def contact(request):

    return render(request, 'store/contact.html')


def tips(request):
    #find the healthtips from the database

    token = TOKEN
    url_healthtip = 'https://admin.nugarypharmacy.com/api/healthtips'
    url_category = 'https://admin.nugarypharmacy.com/api/healthtipCategory'

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
    url = 'https://admin.nugarypharmacy.com/api/healthtips'

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
    # pass the subtotal amount to the purchase page

    if 'buy_now' in request.GET and request.GET['buy_now'] == "1":
        return render(request, 'store/purchase.html',
                    {'subtotal': 'Please contact us(+234 8169188795 or +234 8163106125) to get the current price of this product'})
    
    else:
        if 'subtotal' in request.session:
            subtotal = request.session['subtotal']
        else:
            subtotal = 0    

        return render(request, 'store/purchase.html',
                    {'subtotal': subtotal})


def update_cart(request):
    # delete a product from the cart and update the cart


    if request.method == 'POST':
        name = request.POST['product_name']
        cart = request.session['cart']

        index = 0
        qty = 0
        price = 0
        for item in cart:
            if item['name'] == name:
                # get the quantity and total price of the product to be deleted
                qty = int(item['quantity'])
                price = int(item['price'])
                cart.pop(index)
                break
            index += 1   
        # update the data in the session     
        request.session['cart'] = cart 
        count = request.session['total_products'] 
        count = count - qty
        request.session['total_products'] = count
        subtotal = request.session['subtotal'] 
        subtotal = subtotal - price
        request.session['subtotal'] = subtotal  
        # clear the cart if the cart is empty
        if subtotal == 0:
            request.session['cart'] = None
            request.session['total_products'] = None
            request.session['subtotal'] = None

        return redirect('view_cart')
       

def view_cart(request):
    # display the products in the cart

    # display the product categories
    token = TOKEN
    url_category = 'https://admin.nugarypharmacy.com/api/productCategory'
    params = {'token': token}
    response2 = requests.get(url_category, params)
    if response2.status_code == 200:
        categories = response2.json() 
    else:
        categories = []

    if request.method == "POST":
        # store product in session
        name = request.POST['productName']
        img = request.POST['productImg']
        quantity = request.POST['productQty']
        price = request.POST['productPrice']
       
        try:   
            price = int(quantity) * int(price)
        except ValueError:
            quantity = 1
            price = int(quantity) * int(price)    

        # a dictionary to store product details
        product = {'name': name, 'quantity': quantity,
                   'price': price, 'image_url': img}
        
        if 'cart' in request.session:
            # check if any prduct exist in cart
            cart = request.session['cart']
            # check if product already exist in cart
            index = 0
            foundMatch = False
            for item in cart:
                if item['name'] == product['name']:
                    # if product exists, replace the old entry with the new one
                    cart[index] = product
                    foundMatch = True
                index += 1

            # update session data    
            if not foundMatch:
                # if product does not exist add it to session
                cart.append(product)
                # calculate subtotal price and total quantity of products in cart
                sub_total = 0
                total_qty = 0
                for item in cart:
                    sub_total += int(item['price']) 
                    total_qty += int(item['quantity'])
                request.session['cart'] = cart
                request.session['total_products'] = total_qty
                request.session['subtotal'] = sub_total
            else:
                # calculate subtotal price and total quantity of products in cart
                sub_total = 0
                total_qty = 0
                for item in cart:
                    sub_total += int(item['price']) 
                    total_qty += int(item['quantity'])
                request.session['cart'] = cart
                request.session['total_products'] = total_qty
                request.session['subtotal'] = sub_total
    
        else:
            cart = [product]
            request.session['cart'] = cart
            request.session['total_products'] = product['quantity']
            request.session['subtotal'] = product['price']

        return render(request, 'store/view_cart.html', 
                      {'cart': cart, 'count': request.session['total_products'],
                       'subtotal': request.session['subtotal'],
                       'categories': categories})

    else: 
        if 'cart' in request.session:
            cart = request.session['cart']
            return render(request, 'store/view_cart.html', 
                    {'cart': cart, 'count': request.session['total_products'],
                       'subtotal': request.session['subtotal'],
                       'categories': categories})
        else:
            return render(request, 'store/view_cart',
                          {'categories': categories})
        







    