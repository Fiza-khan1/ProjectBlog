from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Blogapp.urls')),  # Direct root URL to Blogapp URLs
    path('', include('users.urls')),  # Assuming users-related URLs start with 'users/'
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
