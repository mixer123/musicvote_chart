from django.urls import path, include
from . import views

app_name = "songs"

urlpatterns = [
    # path("", views.index, name="index"),
    path("", views.songs, name="songs"),
    path('song/<int:id>/', views.song_detail, name="song-detail"),
    path('ip/', views.get_ip, name="ip"),
    path('ranking/', views.ranking, name="ranking"),
# path('image/', views.index_view, name="index_view"),


]