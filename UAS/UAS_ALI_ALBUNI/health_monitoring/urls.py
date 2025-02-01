# health/urls.py
from django.urls import path
from .views import record_activity

urlpatterns = [
    path('record_activity/', record_activity, name='record_activity'),
]

# health_monitoring/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health.urls')),
]
