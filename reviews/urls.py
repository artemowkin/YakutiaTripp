from django.urls import path

from . import views


urlpatterns = [
    path('', views.AllReviewsView.as_view(), name='all_reviews'),
    path(
        '<uuid:pk>/', views.SetReviewAvatarView.as_view(),
        name='set_review_avatar'
    ),
]
