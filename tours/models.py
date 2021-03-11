import uuid

from django.db import models


class Tour(models.Model):
    """Model of tour"""

    uuid = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4
    )
    title = models.CharField(max_length=255)
    preview = models.ImageField(upload_to='tours')
    short_description = models.CharField(max_length=4000)
    about = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    city_from = models.CharField(max_length=255)
    city_to = models.CharField(max_length=255)
    views = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title


class TourDay(models.Model):
    """Model of tour day"""

    WEEKDAYS = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday')
    ]
    weekday = models.CharField(choices=WEEKDAYS, max_length=9)
    description = models.TextField()
    tour = models.ForeignKey(
        Tour, on_delete=models.CASCADE, related_name="days"
    )

    def __str__(self):
        return self.description
