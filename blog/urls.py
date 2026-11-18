
from django.urls import path
from .views import Post, PostDetail

urlpatterns = [
    path("post/", Post.as_view(), name="post"),
    path(
        "post/<slug:slug>/",
        PostDetail.as_view(),
        name="post_detail"
    ),
]
