from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .api import ExampleApiQuery
from .settings import CONFIG


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("api/v1/", include("app_users.urls")),
    path("sentry-debug/", trigger_error),
    path(
        "api/v1/api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path("api/v1/example/", ExampleApiQuery.as_view(), name="example_api"),
    path("api/v1/test/", TokenRefreshView.as_view(), name="test"),
    path("api/v1/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/v1/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/v1/swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if CONFIG.debug:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
