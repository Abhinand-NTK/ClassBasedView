from django.db import models
from django.utils.text import slugify
# Create your models here.


class Blog(models.Model):

    title = models.CharField(max_length=100)
    content = models.TextField()

    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            self.slug = base_slug

            # Check for unique constraint violation and handle it
            count = 2
            while Blog.objects.filter(slug=self.slug).exists():
                self.slug = f"{base_slug}-{count}"
                count += 1

        super().save(*args, **kwargs)