from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

admin.autodiscover()

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns(
    '',
    url(r'^$', TemplateView.as_view(template_name='homepage.html')),
    url(r'^feed/$', TemplateView.as_view(template_name='feed.html')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
