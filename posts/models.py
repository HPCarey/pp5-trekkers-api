from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):

    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    This model is adapted from the Ci moments walkthrough model
    but contains some custom fields
    """

    DIFFICULTY_CHOICES = [
        ('EA', 'Easy'),
        ('MO', 'Moderate'),
        ('CH', 'Challenging'),
        ('DI', 'Difficult'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    country = models.CharField(max_length=50)
    location = models.CharField(max_length=255, blank=True)
    difficulty = models.CharField(
        max_length=300,
        choices=DIFFICULTY_CHOICES,
        default=none
    )
    rating = models.IntegerField()
    image = models.ImageField(
        upload_to='images/', default='../default_post_cgvnmr', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.event_title} {self.date}'
