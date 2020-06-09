from rest_framework import viewsets, permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .filters import TrackFiler
from .models import Track, Album, Genre
from .serializers import TrackChangeSerializer, TrackReadSerializer, AlbumSerializer, GenreSerializer
from .permissions import IsOwnerOrReadOnly


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    filterset_class = TrackFiler
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ['musician__username', 'title']
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(musician=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list' or self.action == "retrieve":
            return TrackReadSerializer
        return TrackChangeSerializer


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(musician=self.request.user)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
