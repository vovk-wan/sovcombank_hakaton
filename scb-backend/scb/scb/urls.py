from django.contrib import admin
from django.urls import include, path

from .settings import CONFIG

urlpatterns = [
    path("api-auth/", include("rest_framework.urls")),
    path("admin/", admin.site.urls),
]

if CONFIG.debug:
    urlpatterns.append(
        path("__debug__/", include("debug_toolbar.urls")),
    )
