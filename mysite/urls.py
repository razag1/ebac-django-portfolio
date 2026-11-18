
from django.contrib import admin
from django.urls import include, path
from blog.views import PostList

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("blog.urls")),
    path("", PostList.as_view(), name="home"),
]
