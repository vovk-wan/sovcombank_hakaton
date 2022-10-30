from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api import TestView

from .settings import CONFIG


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path("admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
    path("api/v1/api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("api/v1/test/", TokenRefreshView.as_view(), name="test"),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]

if CONFIG.debug:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
