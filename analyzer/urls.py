from django.contrib import admin
from django.urls import path, include
from core.views import home  # Import the home view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Serve index.html at /
    path('analyze/', include('core.urls')),  # Ensure analyze/ URL works
]
