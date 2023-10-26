from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['show_image_box', 'title', 'score', 'create_date']
    list_editable = ['score']
