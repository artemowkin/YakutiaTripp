import uuid

from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Review(models.Model):
    """Review model"""

    uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    name = models.CharField(max_length=255)
    avatar = models.ImageField(
        upload_to='reviews', default='/reviews/default_review_avatar.jpg'
    )
    rating = models.PositiveSmallIntegerField(validators=[
        MaxValueValidator(5), MinValueValidator(1)
    ])
    text = models.CharField(max_length=4000)
    moderated = models.BooleanField(default=False)
    pub_date = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('moderated', '-rating')

    def __str__(self):
        return self.name
