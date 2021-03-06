import uuid

from django.db import models


class News(models.Model):
    """Model of news"""

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    title = models.CharField(max_length=255, unique=True)
    preview = models.ImageField(upload_to="news")
    text = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        ordering = ('-pub_date', 'title')
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
