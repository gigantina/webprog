from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('faq', views.faq, name='faq'),
    path('genres', views.genres, name='genres'),
    path('compositions', views.compositions, name='compositions'),
    path('authors', views.authors, name='authors'),
    path('authors/<int:author_id>/', views.author, name='author'),
    path('perfomances', views.perfomances, name='perfomances'),
    path('compositions/<int:composition_id>/', views.composition, name='composition')
]
