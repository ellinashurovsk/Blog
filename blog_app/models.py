from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='Slug')
    body = models.TextField(verbose_name='Content')
    date_added = models.DateTimeField(
        auto_now_add=True, verbose_name='Date added')
    date_updated = models.DateTimeField(
        auto_now=True, verbose_name='Date updated')
    owner = models.ForeignKey(
        User, related_name='posts', on_delete=models.CASCADE, verbose_name='Owner')

    def __str__(self):
        """Return a string representation of the model."""
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
