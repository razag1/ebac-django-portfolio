
from django.http import HttpResponse
from django.views.generic import View, ListView, DetailView
from .models import Post as PostModel


class Post(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello World")


class PostList(ListView):
    model = PostModel
    template_name = "index.html"
    context_object_name = "post_list"

    def get_queryset(self):
        return PostModel.objects.filter(
            status=PostModel.Status.PUBLISHED
        ).exclude(
            slug__isnull=True
        ).exclude(
            slug=""
        ).order_by("-created_at")


class PostDetail(DetailView):
    model = PostModel
    template_name = "post_detail.html"
    context_object_name = "post"
    slug_field = "slug"

    def get_queryset(self):
        return PostModel.objects.filter(
            status=PostModel.Status.PUBLISHED
        )
