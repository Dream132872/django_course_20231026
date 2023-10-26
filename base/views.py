from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from slider import models


def home_page_view(request: HttpRequest):
    context = {}
    return render(request, 'base/index.html', context)


def about_us_view(request: HttpRequest):
    return render(request, 'base/about-us.html')
