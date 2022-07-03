from django.db import models
from .validators import validate_trailer_size
from PIL import Image
from django.utils.text import slugify

# Create your models here.

MOVIE_CATEGORIES = (
    ("Documentary Film", "Documentary Film"),
    ("Feature Film", "Feature Film"),
    ("Short Film", "Short Film"),
    ("Student Film", "Student Film"),
    ("Women in Film", "Women in Film"),
    ("Animated Film", "Animated Film"),
    ("African Films", "African Films"),
)

GENRES = (
    ("Action", "Action"),
    ("Adult", "Adult"),
    ("Adventure", "Adventure"),
    ("Children's/Family", "Children's/Family"),
    ("Comedy", "Comedy"),
    ("Comedy Drama", "Comedy Drama"),
    ("Crime", "Crime"),
    ("Drama", "Drama"),
    ("Epic", "Epic"),
    ("Fantasy", "Fantasy"),
    ("Historical", "Historical"),
    ("Horror", "Horror"),
    ("Musical", "Musical"),
    ("Mystery", "Mystery"),
    ("Romance", "Romance"),
    ("Science Fiction", "Science Fiction"),
    ("Spy", "Spy"),
    ("Thriller", "Thriller"),
    ("War", "War"),
    ("Other", "Other"),
)


class Genres(models.Model):
    genre = models.CharField(choices=GENRES, max_length=255)


class SubmitFilm(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=70, choices=MOVIE_CATEGORIES)
    poster = models.ImageField(upload_to="official_posters")
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=100, blank=True)
    genres = models.ManyToManyField(Genres, blank=True,)
    country = models.CharField(max_length=100, blank=True)
    directors = models.CharField(max_length=100, blank=True)
    writers = models.CharField(max_length=100, blank=True)
    producers = models.CharField(max_length=100, blank=True)
    key_casts = models.TextField(blank=True)
    about_submitter = models.TextField(blank=True)
    user_score = models.IntegerField(default=0)
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


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="gallery")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
