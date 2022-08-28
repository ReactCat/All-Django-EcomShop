from django.shortcuts import render, get_object_or_404
from store.models import Product
from category.models import Category



def home(request):
    
    products = Product.objects.all().filter(is_available=True)

    return render(request, "store/home.html", { 'products': products} )



def products(request, category_slug=None):
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category = categories, is_available=True)
        product_count = products.count()
    
    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
    
    return render(request, "products/products.html", 
    { 'products': products, 'productcount': product_count} )


def product_detail(request, category_slug, product_slug):

    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e


    return render(request, "products/product_detail.html", {'single_product': single_product})

