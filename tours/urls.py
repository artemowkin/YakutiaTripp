from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllToursView.as_view(), name='all_tours'),
]
