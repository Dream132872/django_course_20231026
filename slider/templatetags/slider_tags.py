from django import template
import datetime
from base import date_convertor
from .. import models

register = template.Library()


@register.inclusion_tag('slider/slider_box.html')
def show_slider_box(*args, **kwargs):
    sliders = models.Slider.objects.order_by('-display_order').all()
    return {
        'sliders': sliders
    }
