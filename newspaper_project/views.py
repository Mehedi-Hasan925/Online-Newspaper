from django.shortcuts import render,HttpResponseRedirect
# from newspaper_project import forms
from newspaper_project import models
from django.apps import apps
from django.core.paginator import Paginator

# Create your views here.
def home(request):
    top_news_bd = models.Bangladesh.objects.all()[:1]
    top_news_int = models.International.objects.all()[:1]
    top_news_ent = models.Entertainment.objects.all()[:1]
    top_news_trd = models.Trade.objects.all()[:1]
    top_news_sports = models.Sports.objects.all()[:1]
    top_news = {'top_news_sports':top_news_sports, 'top_news_trd':top_news_trd, 'top_news_ent':top_news_ent, 'top_news_int':top_news_int, 'top_news_bd':top_news_bd}

    bangladesh_news = models.Bangladesh.objects.all()[:6]
    international_news = models.International.objects.all()[:6]
    trade_news = models.Trade.objects.all()[:6]
    entertainment_news = models.Entertainment.objects.all()[:6]
    sports_news = models.Sports.objects.all()[:6]

    diction = {'top_news':top_news,'bangladesh_news':bangladesh_news, 'trade_news':trade_news, 'international_news':international_news, 'entertainment_news':entertainment_news, 'sports_news':sports_news}
    return render(request,'newspaper_project/home.html',context=diction)


def news_details(request,pk,table):
    news = getattr(models, table).objects.get(pk=pk)
    related_news = getattr(models, table).objects.exclude(pk=pk)[:5]
    # paginator = Paginator(related_news, )
	# page_number = request.GET.get('page')
	# page_obj = paginator.get_page(page_number)
    diction = {'news':news,'related_news':related_news}
    return render(request,'newspaper_project/news_details.html',context=diction)


def news_Bangladesh(request):
    news = models.Bangladesh.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    diction = {'page_obj':page_obj, 'headline':'বাংলাদেশ'}
    return render(request,'newspaper_project/news_all.html',context=diction)


def news_International(request):
    news = models.International.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    diction = {'page_obj':page_obj, 'headline':'আন্তর্জাতিক'}
    return render(request,'newspaper_project/news_all.html',context=diction)

def news_Trade(request):
    news = models.Trade.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    diction = {'page_obj':page_obj, 'headline':'বাণিজ্য'}
    return render(request,'newspaper_project/news_all.html',context=diction)

def news_Entertainment(request):
    news = models.Entertainment.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    diction = {'page_obj':page_obj, 'headline':'বিনোদন'}
    return render(request,'newspaper_project/news_all.html',context=diction)

def news_Sports(request):
    news = models.Sports.objects.all()
    paginator = Paginator(news,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    diction = {'page_obj':page_obj, 'headline':'খেলাধুলা'}
    return render(request,'newspaper_project/news_all.html',context=diction)

