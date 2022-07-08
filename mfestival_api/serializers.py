from rest_framework import serializers
from .models import SubmitFilm, Gallery, ContactUs, JoinBsiff


class SubmitFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitFilm
        fields = ['id', 'title', 'category', 'poster', 'views', 'duration', 'description', 'language',
                  'trailer', 'genre', 'country', 'directors', 'writers', 'producers', 'key_casts', 'about_submitter',
                  'movie_link', 'user_score',
                  'slug', 'date_posted', 'selected', 'full_movie', 'festival_date', 'get_movie_poster',
                  'get_movie_trailer', 'get_full_movie']


class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'title', 'image', 'date_posted', 'get_image']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = ['id', 'first_name', 'last_name', 'email', 'message', 'date_contacted']


class JoinBsiffSerializer(serializers.ModelSerializer):
    class Meta:
        model = JoinBsiff
        fields = ['id', 'full_name', 'email', 'date_joined']
