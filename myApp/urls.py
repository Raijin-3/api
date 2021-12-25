from django.urls import path
from .views import AddArticle, AllArticle


urlpatterns = [
    path('new', AddArticle.as_view() ),
    path('all', AllArticle.as_view())
]