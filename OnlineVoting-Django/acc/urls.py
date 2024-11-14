from django.urls import path , re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve



urlpatterns = [
    
    
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.account_login, name="account_login"),
    path('register/', views.account_register, name="account_register"),
    path('logout/', views.account_logout, name="account_logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
