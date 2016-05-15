from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.db.models import Q

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView

from digitalmarket.mixins import MultiSlugMixin, SubmitBtnMixin, LoginRequiredMixin
from .mixins import ArticleManagerMixin

#import models
from .models import Article

#import forms
from .forms import ArticleModelForm
# Create your views here.

class ArticleCreateView(LoginRequiredMixin, SubmitBtnMixin, CreateView):
    model = Article
    form_class = ArticleModelForm
    submit_btn = "Add Article"

    def form_valid(self, form):
        user = self.request.user
        form.instance.user = user
        valid_data = super(ArticleCreateView, self).form_valid(form)
        #add all default users
        return valid_data

class ArticleUpdateView(ArticleManagerMixin,SubmitBtnMixin, MultiSlugMixin, UpdateView):
    model = Article
    form_class = ArticleModelForm
    submit_btn = "Update Article"

class ArticleListView(ListView):
    model = Article

    def get_queryset(self, *args, **kwargs):
        qs = super(ArticleListView, self).get_queryset(**kwargs)
        querry = self.request.GET.get("q")
        if querry:
            qs = qs.filter(
                Q(title__icontains=querry)
            )
        return qs.order_by("title")

class ArticleDetailView(MultiSlugMixin, DetailView):
    model = Article