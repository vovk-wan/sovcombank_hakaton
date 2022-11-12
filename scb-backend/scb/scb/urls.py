from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)

from .settings import CONFIG

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


def trigger_error(request):
    division_by_zero = 1 / 0
    print(division_by_zero)


urlpatterns = [
    path("api/v1/admin/", admin.site.urls),
    path("sentry-debug/", trigger_error),
    path(
        "api/v1/api-auth/", include("rest_framework.urls",
                                    namespace="rest_framework")
    ),
    path("api/v1/test/", TokenRefreshView.as_view(), name="test"),
    path("api/v1/token/", TokenObtainPairView.as_view(),
         name="token_obtain_pair"),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(),
         name="token_refresh"),
    re_path(
        r"^api/v1/swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    re_path(
        r"^api/v1/swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    re_path(
        r"^api/v1/redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

if CONFIG.debug:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
