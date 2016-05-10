from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(blank=True) #unique=True
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2, default=0)
    sale_price = models.DecimalField(max_digits=100, decimal_places=2, null=True, blank=True)

    def __unicode__(self):
        return self.title

def product_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)

pre_save.connect(product_pre_save_receiver, sender=Product)