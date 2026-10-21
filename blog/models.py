
from django.db import models


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
