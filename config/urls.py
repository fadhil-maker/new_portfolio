from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

from django.views.generic import TemplateView

urlpatterns = [
    path('hq-portal/', admin.site.urls),
    path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),
    path('sitemap.xml', TemplateView.as_view(template_name='sitemap.xml', content_type='application/xml')),
    path('google85acb267c92167a0.html', TemplateView.as_view(template_name='google85acb267c92167a0.html', content_type='text/html')),
    path('llms.txt', TemplateView.as_view(template_name='llms.txt', content_type='text/plain')),
    path('', include('apps.core.urls')),
]

if settings.DEBUG:
    urlpatterns += [
        path('__reload__/', include('django_browser_reload.urls')),
    ]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
