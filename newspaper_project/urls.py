from django.urls import path
from newspaper_project import views

app_name = 'newspaper_project'

urlpatterns = [
    path('', views.home, name='home'),
    path('news_details/<pk>/<table>', views.news_details, name='news_details'),
    path('news_Bangladesh/', views.news_Bangladesh, name='news_Bangladesh'),
    path('news_International/', views.news_International, name='news_International'),
    path('news_Trade/', views.news_Trade, name='news_Trade'),
    path('news_Entertainment/', views.news_Entertainment, name='news_Entertainment'),
    path('news_Sports/', views.news_Sports, name='news_Sports'),
    
]