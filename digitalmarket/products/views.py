from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Q

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from digitalmarket.mixins import MultiSlugMixin, SubmitBtnMixin, LoginRequiredMixin
from .mixins import ProductManagerMixin

#import models
from .models import Product

#import forms
from .forms import ProductModelForm
# Create your views here.

class ProductCreateView(LoginRequiredMixin, SubmitBtnMixin, CreateView):
    model = Product
    form_class = ProductModelForm
    submit_btn = "Add Product"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ProductCreateView, self).form_valid(form)
        form.instance.managers.add(user)
        #add all default users
        return valid_data

class ProductUpdateView(ProductManagerMixin,SubmitBtnMixin, MultiSlugMixin, UpdateView):
    model = Product
    form_class = ProductModelForm
    submit_btn = "Update Product"

class ProductListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs = super(ProductListView, self).get_queryset(**kwargs)
        querry = self.request.GET.get("q")
        if querry:
            qs = qs.filter(
                Q(title__icontains=querry)
            )
        return qs.order_by("title")

class ProductDetailView(MultiSlugMixin, DetailView):
    model = Product