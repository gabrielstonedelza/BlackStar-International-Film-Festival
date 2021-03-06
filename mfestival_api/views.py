from django.shortcuts import get_object_or_404
from .models import SubmitFilm, Gallery, ContactUs, JoinBsiff
from .serializers import SubmitFilmSerializer, GallerySerializer, ContactSerializer, JoinBsiffSerializer
from rest_framework import filters
from django.db.models import Q
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def join_bsiff(request):
    serializer = JoinBsiffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_join_bsiff_lists(request):
    bsiffs = JoinBsiff.objects.all().order_by('-date_joined')
    serializer = JoinBsiffSerializer(bsiffs, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def contact_us(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_contact_lists(request):
    contacts = ContactUs.objects.all().order_by('-date_contacted')
    serializer = ContactSerializer(contacts, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def submit_film(request):
    serializer = SubmitFilmSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_submitted(request):
    devotions = SubmitFilm.objects.all().order_by('-date_posted')
    serializer = SubmitFilmSerializer(devotions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_selected(request):
    devotions = SubmitFilm.objects.filter(selected=True).order_by('-date_posted')
    serializer = SubmitFilmSerializer(devotions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def film_detail(request, slug):
    film = get_object_or_404(SubmitFilm, slug=slug)
    if film:
        film.views += 1
        film.save()
    serializer = SubmitFilmSerializer(film, many=False)
    return Response(serializer.data)


@api_view(['GET', 'PUT'])
@permission_classes([permissions.AllowAny])
def add_to_selected(request, slug):
    selected_film = get_object_or_404(SubmitFilm, slug=slug)
    serializer = SubmitFilmSerializer(selected_film, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_gallery(request):
    gallery = Gallery.objects.all().order_by('-date_posted')
    serializer = GallerySerializer(gallery, many=True)
    return Response(serializer.data)


class GetFilm(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = SubmitFilm.objects.all().order_by('-date_posted')
    serializer_class = SubmitFilmSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title']
