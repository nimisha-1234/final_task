from django.urls import path
from . import views
from .views import search_movies

app_name = 'movieapp'

urlpatterns = [

    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.details, name="details"),
    path('add/', views.add_movie, name='add_movie'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('search/', search_movies, name='search_movies'),
    #path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),
]