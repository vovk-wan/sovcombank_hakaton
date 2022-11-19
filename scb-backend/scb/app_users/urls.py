from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from app_users.api import ProfileListApiView, RegistrationApiView

urlpatterns = [
    path("register/", RegistrationApiView.as_view(), name="registration_api_view"),
    path("profiles/", ProfileListApiView.as_view()),
]
