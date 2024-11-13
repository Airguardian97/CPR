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
    path('', include('acc.urls')),
    path('accounts/', include('allauth.urls')),
    # path('accounts/google/login/', OAuth2LoginView.as_view(), name='google_login'),
    # path('login', TemplateView.as_view(template_name='account/login.html'), name="login"),
    path('acc/', include('acc.urls')),
    path('admin/', admin.site.urls),
    path('administrator/', include('administrator.urls')),
    path('voting/', include('voting.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

