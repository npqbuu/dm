from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.utils.text import slugify
from django.conf import settings
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField

def download_media_location(instance, filename):
    return "%s/%s" %(instance.id, filename)

# Create your models here.
class Product(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    managers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="managers_products", blank=True)
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True, unique=True)
    description = HTMLField(null=True, blank=True)
    price = models.DecimalField(max_digits=100, decimal_places=0, default=0)
    sale_price = models.DecimalField(max_digits=100, decimal_places=0, null=True, blank=True)
    media = models.ImageField(blank=True, null=True,
                             upload_to=download_media_location,

    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        view_name = "products:detail_slug"
        return reverse(view_name, kwargs={"slug" : self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)

    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).exists()
    if qs:
        new_slug="%s-%s" %(slug, instance.id)
        return create_slug(instance, new_slug=new_slug)

    return slug

def product_post_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)
        instance.save()
    if not instance.sale_price:
        instance.sale_price = float(instance.price) * 2
        instance.save()

post_save.connect(product_post_save_receiver, sender=Product)