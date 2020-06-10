from rest_framework import serializers

from .models import Track, Album, Genre


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(musician=request.user)


class TrackChangeSerializer(serializers.ModelSerializer):
    album = UserFilteredPrimaryKeyRelatedField(queryset=Album.objects, required=False)

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ('musician',)


class TrackReadSerializer(serializers.ModelSerializer):
    musician = serializers.CharField(read_only=True)
    genre = serializers.CharField()
    album = serializers.CharField()

    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    musician = serializers.CharField(read_only=True)
    tracks = TrackReadSerializer(many=True, required=False)

    class Meta:
        model = Album
        fields = '__all__'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'
