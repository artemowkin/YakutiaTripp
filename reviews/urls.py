from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllReviewsView.as_view(), name='all_reviews'),
]
