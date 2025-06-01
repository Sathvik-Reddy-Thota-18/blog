from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.


# Retriving the models
articles = Article.objects.all()


def home(request):

    search = request.GET.get('search')

    results = articles

    #Django method of filtering
    if search:
        results = articles.filter(title__icontains = search) or articles.filter(author__icontains = search)

    # # This is also a Working Procedure but we use django retriving methods
    # if search:
    #     results = [article for article in articles if search.lower() in article.title.lower() or search.lower() in article.author.lower()]   
    
    context = {
        'title':'Home',
        'articles':results
    }

    return render(request,'home.html',context)




def article(request, id):

    try:
        retrived_article = Article.objects.get(id = id)
    except:
        retrived_article = None


    # for article_data in articles:
    #     if article_data["id"] == id:
    #         retrived_article = article_data
    #         break

    context = {
        'title':'article',
        'article': retrived_article
    }

    return render(request,'article.html',context)




def about(request):
    context = {
        'title':'about'
    }
    return render(request,'about.html',context)




def contact(request):
    context = {
        'title':'contact'
    }
    return render(request,'contact.html',context)