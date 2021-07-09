from django.shortcuts import render,HttpResponseRedirect
from newspaper_project import models
from admin_section import  forms
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse,reverse_lazy
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def log_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user =  authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}
    return render(request,'admin_section/login.html',context=diction)

@login_required
def news_admin(request):
    diction = {}

    return render(request,'admin_section/admin_page.html',context=diction)


@login_required
def admin_bangladesh(request):
    form = forms.Banglades_news()
    if request.method == 'POST':
        form = forms.Banglades_news(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}

    return render(request,'admin_section/admin_bangladesh.html',context=diction)


@login_required
def admin_international(request):
    form = forms.International_news()
    if request.method == 'POST':
        form = forms.International_news(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}

    return render(request,'admin_section/admin_international.html',context=diction)


@login_required
def admin_entertainment(request):
    form = forms.Entertainment_news()
    if request.method == 'POST':
        form = forms.Entertainment_news(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}

    return render(request,'admin_section/admin_ent.html',context=diction)


@login_required
def admin_sports(request):
    form = forms.Sports_news()
    if request.method == 'POST':
        form = forms.Sports_news(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}

    return render(request,'admin_section/admin_sports.html',context=diction)


@login_required
def admin_trade(request):
    form = forms.Trade_news()
    if request.method == 'POST':
        form = forms.Trade_news(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_section:news_admin'))
    diction = {'form':form}

    return render(request,'admin_section/admin_trade.html',context=diction)
