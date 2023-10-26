from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.


def products_list_view(request: HttpRequest):
    return render(request, 'products_list.html')
