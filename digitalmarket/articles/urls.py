from django.conf.urls import url

#import views
from . import views


urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='list'),
    url(r'^add/$',views.ArticleCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$',views.ArticleDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$',views.ArticleDetailView.as_view(), name='detail_slug'),
    url(r'^(?P<pk>\d+)/edit/$',views.ArticleUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$',views.ArticleUpdateView.as_view(), name='update_slug'),
]
