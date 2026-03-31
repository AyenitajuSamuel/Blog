from django.urls import path
from .views import post_list, post_detail, post_create

urlpatterns = [
    path("", post_list, name='post_list'),
    path("posts/<int:pk>/", post_detail, name='post_detail'),
    path("posts/create/", post_create, name="post_create"),
]
