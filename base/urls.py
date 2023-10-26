from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page_view, name='home_view'),
    path('about-us/', views.about_us_view, name='about_us_view')
]

