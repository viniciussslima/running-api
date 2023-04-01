from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from events.views import EventViewSet

app_name = "events"
router = DefaultRouter()
router.register("", EventViewSet, basename="events")


urlpatterns = [
    path("", include(router.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
