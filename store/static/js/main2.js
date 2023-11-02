/* ------------main.js 2-------------*/
/*--------limit the number of characters in the paragraph for healthtips*/
document.addEventListener('DOMContentLoaded', 
function () {
      const paragraphs = document.getElementsByClassName('description');

      for (let i = 0; i < paragraphs.length; i++) {
        const inputText = paragraphs[i].textContent;
        const limit = 300;
        const end = ' .....Click on heading to read.....';
        if (inputText.length > limit) {
            paragraphs[i].textContent = inputText.substring(0, limit) + end;
          }
          
        }
      
    });

    /*---------the blog page(all healthtips page)---------*/
document.addEventListener('DOMContentLoaded', 
function () {
        const paragraphs = document.getElementsByClassName('blog-description');

        for (let i = 0; i < paragraphs.length; i++) {
        const inputText = paragraphs[i].textContent;
        const limit = 100;
        const end = ' .....';
        if (inputText.length > limit) {
            paragraphs[i].textContent = inputText.substring(0, limit) + end;
            }
            
        }
        
    });  
    

/*---this ensures that all '+' in query parameters are converted to '%2B'
before being passed. '%2B' are decoded as '+' when the query parameters are received. 
if this action is not carried out ('+' is received as white-space) it might lead to unexpected results---*/    
var allTags = document.querySelectorAll("a");
for (var i = 0; i < allTags.length; i++) {
    allTags[i].addEventListener('click', function () {
        var queryString = this.getAttribute('href');
            if (queryString.includes('?') === true && queryString.includes('+') === true) {
                var newString = queryString.replaceAll('+', '%2B');
                this.setAttribute('href', newString);
            }
    })
}

/*---this ensures that all '&' in query parameters (except one's seperating query keywords) are converted to '-n6'
before being passed. '-n6' will be reconverted to '&' later. 
if this action is not carried out it might lead to unexpected results---*/    
var allTags = document.querySelectorAll("a");
document.addEventListener('DOMContentLoaded', function (){
    for (var i = 0; i < allTags.length; i++) {
        console.log('ok');
        
            var queryString = allTags[i].getAttribute('href');
                if (queryString.includes('&') === true) {
                    var newString = queryString.replaceAll('&', '-n6');
                        if (newString.includes('-n6brand') === true) {
                            newString = newString.replace('-n6brand', '&brand');
                        }
                        allTags[i].setAttribute('href', newString);
                        console.log('ok2');
                }
        
    }
})


/*---the product-details page---*/    
/*---this fills the form with product details  and submit the form  when
'Add to cart' button is pressed---*/

var addToCartButton = document.querySelector('#product-details .entry-content .add-cart a');
if (addToCartButton !== null) {
    addToCartButton.addEventListener('click', function () {
        var productQuantity = document.querySelector('#product-details .entry-content form .product_quantity');
        var quantityInput = document.querySelector('#product-details .entry-content .qty .qtyBox');
        /*--ensure that the user types in a number into the quantity input box.use 1 instead*/
        if (quantityInput.value !== null) {
            productQuantity.setAttribute('value',quantityInput.value);
        } else {
            productQuantity.setAttribute('value', 1);
        }
        
        document.querySelector('#product-details .entry-content form .submit_btn').click();

    })
}    

/*---the view_cart page----*/
/*---to pass the name of the product to be deleted from the cart---*/
var deleteBtns = document.querySelectorAll('#cart .cart-details .del-btn button');
for (var i=0; i<deleteBtns.length; i++ ) {
    deleteBtns[i].addEventListener('click', function () {
        document.querySelector('#cart form .productToDelete').setAttribute('value', 
        this.getAttribute('title'));
        document.querySelector('#cart form .submit').click();
    })
}

/*---the purchase page---*/
/*---print the delivery fee and total amount when a location is selected--*/
var selectLocator = document.getElementById('select-locations');
if (selectLocator !== null) {
    selectLocator.addEventListener('change', function () {
        var location = this.value;
        console.log(document.querySelector('.account .delivery-fee'));
        var deliveryFee = document.querySelector('.account .delivery-fee').textContent;
        var subTotal = document.querySelector('.account .sub-total').textContent;
        var totalAmount = document.querySelector('.account .amount').textContent;
        console.log(location);
        console.log(deliveryFee);
        console.log(subTotal);
        
        switch (location) {
            case "Agb":
                deliveryFee = "2000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "  " + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "  " + "NGN";
                
                break;
            case "Air":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;
            case "Ala":
                deliveryFee = "1200";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;
            case "Dsc":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;        
            case "Dsr":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;     
            case "Eff":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;     
            case "Egi":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;        
            case "Eke":
                deliveryFee = "800";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Ene":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Hau":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Jak":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Ogh":
                deliveryFee = "3500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;     
            case "Okp":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Oto":
                deliveryFee = "1200";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Ovw":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Owh":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Pti":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
                
                break;     
            case "Ref":
                deliveryFee = "1500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Sed":
                deliveryFee = "500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Ubo":
                deliveryFee = "1500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Ugh":
                deliveryFee = "3000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Usi":
                deliveryFee = "1000";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Usu":
                deliveryFee = "1500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;     
            case "Uto":
                deliveryFee = "1500";
                totalAmount = parseInt(subTotal) + parseInt(deliveryFee);
                document.querySelector('.account .delivery-fee').textContent =  deliveryFee + "NGN";
                document.querySelector('.account .amount').textContent =  totalAmount.toString() + "NGN";
            
                break;                        
            default:
                break;
        }
    })
}

 
