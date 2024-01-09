from django.urls import include, path
from rest_framework import routers

from authentication.views import LoginView

app_name = "authentication"

router = routers.DefaultRouter()
router.register("login", LoginView, basename="login")

urlpatterns = [
    path("", include(router.urls)),
]
