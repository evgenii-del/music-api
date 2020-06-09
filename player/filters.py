from django_filters import rest_framework as filters

from .models import Track


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class TrackFiler(filters.FilterSet):
    genre = filters.CharFilter(field_name='genre__slug')
    album = filters.CharFilter(field_name='album__slug')

    class Meta:
        model = Track
        fields = ['genre', 'album']
