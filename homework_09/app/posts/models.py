from django.db import models
from django.urls import reverse


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    title = models.CharField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return (
            f"{self.title[0:100]}{'...' if len(self.title) > 100 else ''} "
            f"[{self.body[0:100]}{'...' if len(self.body) > 100 else ''}]"
        )

    def get_absolute_url(self):
        return reverse("posts:details", kwargs={"pk": self.pk})

    class Meta:
        ordering = ["-updated_at"]
