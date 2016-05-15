from django.conf.urls import url

#import views
from . import views


urlpatterns = [
    url(r'^$', views.ProductListView.as_view(), name='list'),
    url(r'^add/$',views.ProductCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$',views.ProductDetailView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/$',views.ProductDetailView.as_view(), name='detail_slug'),
    url(r'^(?P<pk>\d+)/edit/$',views.ProductUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[\w-]+)/edit/$',views.ProductUpdateView.as_view(), name='update_slug'),
]
