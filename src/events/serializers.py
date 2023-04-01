from rest_framework import serializers

from .models import Asset, Event


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = [
            "id",
            "url",
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


class EventSerializer(serializers.ModelSerializer):
    certificate = AssetSerializer(read_only=True)
    photos = AssetSerializer(many=True, read_only=True)

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
