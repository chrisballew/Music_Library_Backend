from django.shortcuts import get_list_or_404, get_object_or_404
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Song
from rest_framework import status
from .serializers import SongSerializer
from music_library_app import serializers

@api_view(['GET', 'POST', 'DELETE'])
def songs_list(request):
    if request.method == 'GET':
        music = Song.objects.all()
        serializer = SongSerializer(music, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)




@api_view(['GET', 'PUT', 'DELETE'])
def songs_detail(request, pk):
    music = get_object_or_404(Song, pk=pk)
    if request.method == 'GET':
        serializer = SongSerializer(music);
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SongSerializer(music, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        music.delete()
        serializer = SongSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
        