from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllNewsView.as_view(), name='all_news'),
]
