from django.contrib import admin

# Register your models here.
from .models import Article

class ArticleAdmin(admin.ModelAdmin):
    list_display = ["title","created"]
    search_fields = ["title"]
    class Meta:
        model = Article

admin.site.register(Article, ArticleAdmin)