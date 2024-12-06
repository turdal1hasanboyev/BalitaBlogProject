from django.urls import path
from .views import HomePageView, ArticleDetailView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('single/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
]