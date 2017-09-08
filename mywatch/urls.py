
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView
from watch import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('watch.urls')),
    url(r'^accounts/profile/$', TemplateView.as_view(template_name='watch/account/profile.html')),
    url(r'^testing',TemplateView.as_view(template_name='watch/testing.html')),
    # url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^contact/$', TemplateView.as_view(template_name='watch/contact_us.html')),
    url(r'^about/$', TemplateView.as_view(template_name='watch/about_us.html')),
    url(r'^terms/$', TemplateView.as_view(template_name='watch/terms.html')),
    url(r'^update_session/$', views.update_session),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)