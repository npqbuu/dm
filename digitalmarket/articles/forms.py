from django import forms
from .models import Article
from tinymce.widgets import TinyMCE

PUBLISH_CHOICES = (
    ('publish', "Publish"),
    ('draft', "Draft"),
)


class ArticleModelForm(forms.ModelForm):
    publish = forms.ChoiceField(widget=forms.RadioSelect, choices=PUBLISH_CHOICES, required=True)

    class Meta:
        model = Article
        fields = [
            "title",
            "content",
            "media"
        ]
        widgets = {
            "title" : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'Title'
                }
            ),
            "content" : TinyMCE(
                attrs={
                    'class' : 'form-control',
                    'id' : 'TinyMCE'
                }
            ),
            "media" : forms.ClearableFileInput(
                attrs={
                    'class' : 'form-control',
                }
            )
        }
    def clean(self, *args, **kwargs):
        cleanned_data = super(ArticleModelForm, self).clean(*args, **kwargs)

        return cleanned_data
