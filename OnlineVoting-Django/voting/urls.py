from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, re_path
from django.views.static import serve

urlpatterns = [
   re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('', views.index),
    path('ballot/fetch/', views.fetch_ballot, name='fetch_ballot'),
    path('dashboard/', views.dashboard, name='voterDashboard'),
    path('verify/', views.verify, name='voterVerify'),
    path('verify/otp', views.verify_otp, name='verify_otp'),
    path('otp/resend/', views.resend_otp, name='resend_otp'),
    path('ballot/vote', views.show_ballot, name='show_ballot'),
    path('ballot/vote/preview', views.preview_vote, name='preview_vote'),
    path('ballot/vote/submit', views.submit_ballot, name='submit_ballot'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
