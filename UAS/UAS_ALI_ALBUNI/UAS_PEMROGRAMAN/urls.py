from django.urls import path, include

urlpatterns = [
    path('', include('health.urls')),  # Include health app URLs
]
