from django.shortcuts import render, redirect, get_object_or_404
from .models import Product



# Create your views here.
def all_products(request):
    """ A view to return the membership page """

    products = Product.objects.all()

    context = {
        'products' : products,
    }

    return render(request, 'membership/membership.html', context)


def product_detail(request, product_id):
    """ A view to return the membership detail page """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product' : product,
    }

    return render(request, 'membership/product_detail.html', context)


