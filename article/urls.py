from django.urls import path
from . import views

urlpatterns = [
    # articles/
    path('', views.articles_list_view, name='articles_list_view'),
    path('detail/<int:article_id>', views.article_detail_view, name='articles_detail_view'),
]
