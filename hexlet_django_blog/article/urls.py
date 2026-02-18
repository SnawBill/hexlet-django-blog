from hexlet_django_blog.article import views
from django.urls import path


urlpatterns = [
    path('', views.index),
]