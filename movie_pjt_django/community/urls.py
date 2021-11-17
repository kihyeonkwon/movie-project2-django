from django.urls import path
from . import views


urlpatterns = [
    path('review/', views.ReviewList.as_view()),
    path('review/<int:pk>/', views.ReviewDetail.as_view()),
    path('review/<int:pk>/claps/', views.ReviewClap.as_view()),
    path('review/<int:pk>/comment/', views.Comment.as_view()),
]
