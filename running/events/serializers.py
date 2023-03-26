from rest_framework import serializers

from .models import Event, Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = [
            "id",
            "image",
        ]


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "time",
            "distance",
            "pace",
            "overall_position",
            "age_position",
            "age_category",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id",
            "name",
            "date",
            "time",
            "distance",
            "pace",
            "overall_position",
            "age_position",
            "age_category",
            "certificate",
            "photos",
        ]
