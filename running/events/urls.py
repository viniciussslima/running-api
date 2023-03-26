from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from events.views import EventDetail, EventList

urlpatterns = [
    path("", EventList.as_view()),
    path("<int:pk>/", EventDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
