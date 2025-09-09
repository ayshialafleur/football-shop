import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('jersey', 'Jersey'),
        ('boots', 'Football Boots'),
        ('ball', 'Football'),
        ('equipment', 'Training Equipment'),
        ('accessory', 'Accessories'),
        ('merch', 'Merchandise'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    