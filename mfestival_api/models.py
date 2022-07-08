from email.policy import default

from django.db import models
from .validators import validate_trailer_size
from django.core.validators import FileExtensionValidator
from PIL import Image
from django.utils import timezone
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

supported_files = ["png", "jpg", "jpeg"]
supported_video_files = ["mpeg", "mp4", "mov", ]


class Genres(models.Model):
    genre = models.CharField(choices=GENRES, max_length=255)

    def __str__(self):
        return self.genre


class SubmitFilm(models.Model):
    title = models.CharField(max_length=200, unique=True)
    category = models.CharField(max_length=70, choices=MOVIE_CATEGORIES)
    poster = models.ImageField(upload_to='event_pics', blank=True)
    views = models.IntegerField(default=0)
    duration = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    language = models.CharField(max_length=100, blank=True)
    genre = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    directors = models.TextField(blank=True)
    writers = models.TextField(blank=True)
    producers = models.TextField(blank=True)
    key_casts = models.TextField(blank=True)
    about_submitter = models.TextField(blank=True)
    movie_link = models.URLField(blank=True)
    user_score = models.IntegerField(default=0)
    trailer = models.FileField(blank=True, validators=[validate_trailer_size, FileExtensionValidator(
        allowed_extensions=supported_video_files)], upload_to="trailers")
    slug = models.SlugField(max_length=100, default='', blank=True)
    selected = models.BooleanField(default=False)
    full_movie = models.FileField(max_length=255, upload_to="movies", blank=True, null=True)
    festival_date = models.DateField(auto_now_add=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

    def get_movie_poster(self):
        if self.poster:
            return "http://127.0.0.1:8000" + self.poster.url
        ""

    def get_movie_trailer(self):
        if self.trailer:
            return "http://127.0.0.1:8000" + self.trailer.url
        ""

    def get_full_movie(self):
        if self.full_movie:
            return "http://127.0.0.1:8000" + self.full_movie.url
        ""


class Gallery(models.Model):
    title = models.CharField(max_length=100, blank=True)
    image = models.ImageField(upload_to="gallery")
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_image(self):
        if self.image:
            return "http://127.0.0.1:8000" + self.image.url
        ""


class ContactUs(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    message = models.TextField(default="")
    date_contacted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.first_name


class JoinBsiff(models.Model):
    full_name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True, max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
