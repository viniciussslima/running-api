from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response

from .filters import EventFilter
from .models import Event
from .serializers import EventDetailSerializer, EventListSerializer


class EventList(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventListSerializer
    filter_backends = [SearchFilter, DjangoFilterBackend]
    filterset_class = EventFilter


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventDetailSerializer
    parser_classes = [MultiPartParser, FormParser]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
