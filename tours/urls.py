from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllToursView.as_view(), name='all_tours'),
    path('<uuid:pk>/', views.ConcreteTourView.as_view(), name='concrete_tour'),
]
