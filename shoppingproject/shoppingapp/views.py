from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def index(request):
    return HttpResponse(" I Am Here")


def allProdCat(request, c_slug=None):
    c_page = None
    # products = None
    product_list = None
    # print("From URL:" + str(c_slug))
    if c_slug != None:
        c_page = get_object_or_404(Category, slug=c_slug)
        # products = Product.objects.all().filter(category=c_page, available=True)
        product_list = Product.objects.all().filter(category=c_page, available=True)
        # print("Filtered Products for " + str(c_page))
        # print(products)
    else:
        # products = Product.objects.all().filter(available=True)
        product_list = Product.objects.all().filter(available=True)
    paginator = Paginator(product_list, 6)
    try:
        page = int(request.GET.get('page', 1))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (Emptypage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'category.html', {'category_key': c_page, 'products_key': products})


def proDetail(request, c_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=c_slug, slug=product_slug)
       # print(product.id)
    except Exception as e:
        raise e
    return render(request, 'productdetail.html', {'product_detail_key': product})
