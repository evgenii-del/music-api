from rest_framework import viewsets, permissions

from .models import Track, Album
from .serializers import TrackSerializer, AlbumSerializer
from .permissions import IsOwnerOrReadOnly


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(musician=self.request.user)


class AlbumViewSet(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (IsOwnerOrReadOnly, permissions.IsAuthenticatedOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(musician=self.request.user)
