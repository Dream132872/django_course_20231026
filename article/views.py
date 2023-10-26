from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from .models import Article


# Create your views here.


def articles_list_view(request: HttpRequest):
    # SELECT * FROM article_article
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'article/articles_list.html', context)


def article_detail_view(request: HttpRequest, article_id):
    # try:
    #     article = Article.objects.get(id=article_id)
    # except:
    #     raise Http404('مقاله ای که دنبال آن میگردید یافت نشد')

    article = Article.objects.filter(id=article_id).first()
    if article is None:
        raise Http404('مقاله ای که دنبال آن میگردید یافت نشد')

    context = {
        'article': article
    }
    return render(request, 'article/article_detail.html', context)
