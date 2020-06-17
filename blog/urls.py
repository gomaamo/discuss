from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("signup/", views.UserCreateView.as_view(), name="signup"),
    path("post/", views.PostCreateView.as_view(), name="post"),
    path("posts/<int:pk>", views.PostDetailView.as_view(), name="detail"),
    path("posts/<int:pk>/edit", views.PostEditView.as_view(), name="edit"),
    path("posts/<int:pk>/delete", views.PostDeleteView.as_view(), name="delete"),
    path("users/<int:pk>", views.UserDetailView.as_view(), name="user"),
    path("comments/<int:pk>/delete_comment", views.comment_delete, name="delete_comment"), 
]
