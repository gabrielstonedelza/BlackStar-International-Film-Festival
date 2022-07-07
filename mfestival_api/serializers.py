from rest_framework import serializers
from .models import SubmitFilm, Gallery


class SubmitFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitFilm
        fields = ['id', 'title', 'category', 'poster', 'views', 'duration', 'description', 'language',
                  'trailer', 'genre', 'country', 'directors', 'writers', 'producers', 'key_casts', 'about_submitter',
                  'movie_link', 'user_score',
                  'slug', 'date_posted', 'selected', 'full_movie', 'festival_date', 'get_movie_poster',
                  'get_movie_trailer']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'date_posted', 'get_image']
