from django.contrib import admin
from django.urls import path,include
from bd_news import views

urlpatterns = [

    path('',views.DhakatribuneView, name="dhakatribune_news_link"),
    path('dhakatribune',views.new_link,name='dhakatribune_new_link'),
    path('breaingnews/',views.breakingNews,name='breaking_news_link')


]