from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Post(models.Model):

    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    This model is adapted from the Ci moments walkthrough model
    but contains some custom fields
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    DIFFICULTY_CHOICES = [
        ('Easy', 'Easy'),
        ('Moderate', 'Moderate'),
        ('Challenging', 'Challenging'),
        ('Difficult', 'Difficult'),
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
        default="Easy"
    )
    rating = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(1), MaxValueValidator(5)]
        )
    image = models.ImageField(
        upload_to='images/', default='../default_post_cgvnmr', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
