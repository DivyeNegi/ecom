from django.shortcuts import render
from products.models import Product, Category

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        userName = 'Guest'
    else:
        userName = 'Hi'
    products = Product.objects.all()
    result = []
    bg_color = ["text-bg-dark","bg-body-tertiary"]
    for i in range(0,len(products),2):
        if i+1==len(products):
            break
        color = bg_color if (i//2)%2==0 else bg_color[::-1]
        result.append([products[i],products[i+1]])
        result[-1].extend(color)

    categories = Category.objects.all()

    context = {'products': result, 'categories': categories }

    return render(request, 'home/index.html', context)
