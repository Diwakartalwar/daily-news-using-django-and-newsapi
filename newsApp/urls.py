from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('news-filter/', views.news_filter_page, name='news_filter_page'),
]
