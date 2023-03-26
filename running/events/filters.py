import django_filters
from django_filters import rest_framework as filters

from .models import Event


class EventFilter(filters.FilterSet):
    search = django_filters.CharFilter(field_name="name", lookup_expr="icontains")
    year = filters.NumberFilter(field_name="date__year")
    distance = filters.NumberFilter()

    class Meta:
        model = Event
        fields = ["search", "year", "distance"]
