from django.shortcuts import render, get_object_or_404
from .models import Product
# Create your views here.

def create_view(request):
    #FORM
    template = "create_view.html"
    context = {
    }
    return render(request, template, context)

def detail_slug_view(request, slug=None):
    #1 item
    product = get_object_or_404(Product, slug=slug)
    template = "detail_view.html"
    context = {
        "title" : product.title,
        "description" : product.description,
        "sale_price" : product.sale_price
    }
    return render(request, template, context)

def detail_view(request, object_id=None):
    #1 item
    product = get_object_or_404(Product, id=object_id)
    template = "detail_view.html"
    context = {
        "title" : product.title,
        "description" : product.description,
        "sale_price" : product.sale_price
    }
    return render(request, template, context)

def list_view(request):
    #list of items
    print  request
    queryset = Product.objects.all()
    template = "list_view.html"
    context = {
        "queryset" : queryset
    }
    return render(request, template, context)