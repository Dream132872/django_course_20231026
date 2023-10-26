from django.contrib import admin
from . import models


# Register your models here.


@admin.register(models.Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'url', 'display_order']
    list_editable = ['display_order', 'title']
