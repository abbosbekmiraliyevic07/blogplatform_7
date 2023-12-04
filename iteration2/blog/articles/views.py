from django.shortcuts import render, redirect

# Create your views here.

from .models import *
from .forms import *


# def main(request):
#     articles = Article.objects.all()
#     context = {"articles": articles}
#     return render(request, "main.html", context=context)

def homework(request):
    articles = Article.objects.all()
    return render(request, 'homework.html', {
        'articles': articles
    })


def about(request, pk):
    article = Article.objects.get(pk=pk)

    return render(request, 'about.html', {
        'article': article
    })


def detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, "detail.html", {
        "article": article
    })


def create(request):
    form = ArticleForm(request.POST or None, request.FILES)
    author = request.user
    if request.method == 'POST' and form.is_valid():
        instance = form.save(commit=False)
        instance.author = author
        instance.save()
        return redirect('articles:main')

    return render(request, "create.html", {
        'form': form
    })


def edit(request, slug):
    article = Article.objects.get(slug=slug)
    form = ArticleForm(request.POST or None,
                       request.FILES or None, instance=article)

    if form.is_valid():
        form.save()
        return redirect("articles:detail", slug=request.POST.get('slug'))
    return render(request, "edit.html", {
        "form": form,
        "article": article
    })


def delete(request, slug):
    article = Article.objects.get(slug=slug)

    if request.method == "POST":
        article.delete()
        return redirect("articles:main")
    return render(request, "delete.html", {
        "article": article
    })
