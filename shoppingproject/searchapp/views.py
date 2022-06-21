from django.shortcuts import render
from shoppingapp.models import Product
from django.db.models import Q


def SearchResult(request):
    product = None
    query = None

    #print('REEEEE')
    #print(request.GET)


    if 'q' in request.GET:
        query = request.GET.get('q')
        products = Product.objects.all().filter(Q(name__contains=query) | Q(description__contains=query))
        return render(request, 'search.html', {'query_key': query, 'products_key': products})

# Create your views here.
