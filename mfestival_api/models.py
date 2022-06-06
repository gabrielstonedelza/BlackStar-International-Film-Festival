from django.db import models
from .validators import validate_trailer_size
from PIL import Image
from django.utils.text import slugify

# Create your models here.

MOVIE_CATEGORIES = (
    ("Documentary Film", "Documentary Film"),
    ("Feature Film", "Feature Film"),
    ("Feature Film", "Feature Film"),
    ("Short Film", "Short Film"),
    ("Student Film", "Student Film"),
    ("Women in Film", "Women in Film"),
    ("Animated Film", "Animated Film"),
    ("African Films", "African Films"),
    ("Music Video", "Music Video"),
)


class SubmitFilm(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=70, choices=MOVIE_CATEGORIES)
    poster = models.ImageField(upload_to="official_posters")
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    release_date = models.CharField(max_length=100, blank=True)
    trailer = models.CharField(max_length=100, blank=True, validators=[validate_trailer_size])
    slug = models.SlugField(max_length=100, default='')
    selected = models.BooleanField(default=False)
    festival_date = models.DateField(auto_now_add=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)
