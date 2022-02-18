from django.db import models


class Post(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)
    title = models.CharField(max_length=256)
    body = models.TextField()

    def __str__(self):
        return (
            f"{self.title} [{self.body[0:100]}{'...' if len(self.body) > 100 else ''}]"
        )

    class Meta:
        ordering = ["-updated_at"]
