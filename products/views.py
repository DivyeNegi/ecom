from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .models import Product, Category, ProductImage, Storage, Color
from accounts.models import Order, CartItem

# Create your views here.

def product_view(request, slug):
    try:
        product = Product.objects.get(slug=slug)
        categories = Category.objects.all()
        product_images = product.product_images.all()

        context = {"product": product, 'categories': categories, 'product_images': product_images}

        return render(request, 'product/product.html', context)

    except Exception as e:
        print(e)
        return redirect('/')
    
def add_to_cart(request, uid):
    if not request.user.is_authenticated:
        messages.warning(request, 'Please login first!')
        return redirect('/accounts/login')
    
    product = Product.objects.get(uid=uid)
    user = request.user

    cart, _ = Order.objects.get_or_create(user=user, is_paid=False)

    cartItem = CartItem.objects.create(cart=cart, product=product)

    if request.GET.get('storage'):
        storage = Storage.objects.get(uid=request.GET.get('storage'))
        cartItem.storage = storage
        
    if request.GET.get('color'):
        color = Color.objects.get(uid=request.GET.get('color'))
        cartItem.color = color
    cartItem.save()
    

    return redirect('/accounts/cart')

