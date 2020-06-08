from rest_framework import serializers

from .models import Track, Album


class UserFilteredPrimaryKeyRelatedField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        request = self.context.get('request', None)
        queryset = super(UserFilteredPrimaryKeyRelatedField, self).get_queryset()
        if not request or not queryset:
            return None
        return queryset.filter(musician=request.user)


class TrackSerializer(serializers.ModelSerializer):
    musician = serializers.CharField(read_only=True)
    album = UserFilteredPrimaryKeyRelatedField(queryset=Album.objects)

    class Meta:
        model = Track
        fields = '__all__'


class AlbumSerializer(serializers.ModelSerializer):
    musician = serializers.CharField(read_only=True)
    tracks = TrackSerializer(many=True)

    class Meta:
        model = Album
        fields = '__all__'
