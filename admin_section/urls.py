from django.urls import path
from admin_section import views

app_name = 'admin_section'

urlpatterns = [
    path('', views.log_in, name='login'),
    path('news_admin/', views.news_admin, name='news_admin'),
    path('admin_bangladesh/', views.admin_bangladesh, name='admin_bangladesh'),
    path('admin_international/', views.admin_international, name='admin_international'),
    path('admin_entertainment/', views.admin_entertainment, name='admin_entertainment'),
    path('admin_sports/', views.admin_sports, name='admin_sports'),
    path('admin_trade/', views.admin_trade, name='admin_trade'),
    
]