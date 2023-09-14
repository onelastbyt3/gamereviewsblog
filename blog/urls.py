from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('reviews/', views.ReviewListView.as_view(), name='reviews'),
    path('reviews/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    path('review/<int:pk>/comment/', views.ReviewCommentCreate.as_view(), name='review_comment'),
    path('games/', views.GameListView.as_view(), name='games'),
    path('games/<int:pk>', views.GameDetailView.as_view(), name='game-detail'),
    path('reviewer/<int:pk>', views.ReviewerDetailView.as_view(), name='reviewer-detail'),
    path('requests/', views.ReviewRequestCreate.as_view(), name='review-request'),
    path('requests/success', views.ReviewRequestSuccess, name='review-request-success')
]
