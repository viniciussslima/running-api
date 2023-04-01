from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter

from .models import Event
from .serializers import EventListSerializer, EventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["name"]
    filterset_fields = {
        "date": ["year"],
        "distance": ["exact"],
    }

    def get_serializer_class(self):
        if self.action == "list":
            return EventListSerializer

        return super().get_serializer_class()
