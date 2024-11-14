"""e_voting URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import TemplateView
from . import settings
from allauth.socialaccount.providers.google.views import OAuth2LoginView


urlpatterns = [
    # Include account-related URLs
    path('', include('acc.urls')),  # If you want 'acc.urls' at the root URL

    # Include allauth URLs for authentication
    path('accounts/', include('allauth.urls')),

    # Django admin panel
    path('admin/', admin.site.urls),
    path('acc.', include('acc.urls')), 
    # Include custom URLs for other apps
    path('administrator/', include('administrator.urls')),
    path('voting/', include('voting.urls')),
    
]

# Add media files serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

