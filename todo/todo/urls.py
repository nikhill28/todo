from django.contrib import admin
from django.urls import path, include
from core import urls  # Import the urls module from the core app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(urls)),  # Use 'urls' directly, without 'core'
]
