from django import template

register = template.Library()


@register.filter
def show_currency_type(value):
    return f'{value} تومان'


@register.inclusion_tag('base/site_header.html')
def site_header():
    return {
        'title': 'this is title from inclusion tag'
    }


@register.inclusion_tag('base/site_footer.html')
def site_footer():
    return {}
