# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.discover_view, name='home'),
    path('discover/', views.discover_view, name='discover'),
    path('genre/', views.genre_view, name='genre'),
    path('community/', views.community, name='community'),
    path('trending/', views.trending_view, name='trending'),
    path('favourites/', views.favourites_view, name='favourites'),
    path('playlist/', views.playlist_view, name='playlist'),
    path('signup/', views.signup_view, name='signup'),
    
    path('api/recommend/', views.get_recommendations, name='recommendations_api'),
    path('health/', views.health_check, name='health_check'),
]