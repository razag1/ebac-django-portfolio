
from django.db import models
from django.utils.text import slugify


class Technology(models.Model):
    name = models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    github_url = models.URLField(blank=True)
    technologies = models.ManyToManyField(
        Technology,
        related_name="projects",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Post(models.Model):

    class Status(models.TextChoices):
        DRAFT = "draft", "Rascunho"
        PUBLISHED = "published", "Publicado"

    title = models.CharField(max_length=150)

    slug = models.SlugField(
        max_length=180,
        unique=True,
        blank=True,
        null=True
    )

    content = models.TextField()

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.DRAFT
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)[:180] or "post"
            slug = base_slug
            counter = 2

            while Post.objects.filter(
                slug=slug
            ).exclude(pk=self.pk).exists():
                suffix = f"-{counter}"
                slug = f"{base_slug[:180 - len(suffix)]}{suffix}"
                counter += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

