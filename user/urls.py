from django.urls import path
from .views import (
    UserCreateView, UserDetailView
)

urlpatterns = [
    # User endpoints
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]