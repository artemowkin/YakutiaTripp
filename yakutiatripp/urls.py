from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # ReDoc
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema-url': 'openapi-schema'}
    ), name='redoc'),

    # Local
    path('api/news/', include('news.urls')),
    path('api/tours/', include('tours.urls')),
]
