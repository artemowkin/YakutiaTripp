from django.urls import path, register_converter

from . import views
from .converters import DateConverter


register_converter(DateConverter, 'date')


urlpatterns = [
    path('', views.AllToursView.as_view(), name='all_tours'),
    path('<uuid:pk>/', views.ConcreteTourView.as_view(), name='concrete_tour'),
    path(
        'most_viewed/',
        views.MostViewedToursView.as_view(),
        name='most_viewed_tours'
    ),
    path(
        'search/<str:city_from>/<str:city_to>/<date:date>/',
        views.SearchToursView.as_view(),
        name='search_tours'
    ),
]
