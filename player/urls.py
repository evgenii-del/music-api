from django.urls import path

from . import views

track_list = views.TrackViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

track_detail = views.TrackViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

album_list = views.AlbumViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

album_detail = views.AlbumViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy',
})

urlpatterns = [
    path('tracks/', track_list),
    path('tracks/<int:pk>/', track_detail),
    path('albums/', album_list),
    path('albums/<int:pk>/', album_detail),
]
