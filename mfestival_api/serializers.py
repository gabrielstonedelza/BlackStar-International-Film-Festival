from rest_framework import serializers
from .models import  SubmitFilm


class SubmitFilmSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubmitFilm
        fields = ['id', 'title', 'category', 'poster', 'views', 'duration', 'description', 'release_date', 'trailer',
                  'slug', 'date_posted', 'selected', 'festival_date']
