
from django import forms
from .models import Product
from tinymce.widgets import TinyMCE

PUBLISH_CHOICES = (
    ('publish', "Publish"),
    ('draft', "Draft"),
)

class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            "title",
            "description",
            "price",
            "sale_price",
            "media"
        ]
        widgets = {
            "title" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Title'
                }
            ),
            "description" : TinyMCE(
                attrs={
                    'class' : 'form-control',
                    'id' : 'TinyMCE'
                }
            ),
            "price" : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Price'
                }
            ),
            "sale_price" : forms.NumberInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Sale Price'
                }
            ),
            "media" : forms.ClearableFileInput(
                attrs={
                    'class' : 'form-control',
                }
            )
        }

    def clean(self, *args, **kwargs):
        cleanned_data = super(ProductModelForm, self).clean(*args, **kwargs)

        return cleanned_data

    # def clean_price(self):
    #     price = self.cleanned_data.get("price")
    #     if price < 1.00:
    #         raise forms.ValidationError("Price must be greater than $1.00")
    #     elif price > 99.99:
    #         raise forms.ValidationError("Price must be smaller than $100.00")
    #     else: return price
