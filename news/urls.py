from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllNewsView.as_view(), name='all_news'),
    path('last/', views.LastNewsView.as_view(), name='last_news'),
    path('<uuid:pk>/', views.ConcreteNewsView.as_view(), name='concrete_news'),
]
