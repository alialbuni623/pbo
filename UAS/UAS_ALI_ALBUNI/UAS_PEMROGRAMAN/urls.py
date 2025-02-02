"""URL configuration for UAS_PEMROGRAMAN project."""

from django.contrib import admin
from django.urls import path, include  # Include the path function

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("health.urls")),  # Include the health app URLs
]
