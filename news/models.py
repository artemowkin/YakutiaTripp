from django.db import models


class News(models.Model):
    """Model of news"""

    title = models.CharField(max_length=255)
    preview = models.ImageField(upload_to="news")
    text = models.TextField()
    pub_date = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    def __str__(self):
        return self.title
