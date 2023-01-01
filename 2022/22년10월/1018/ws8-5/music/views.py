from .models import Music , Comment
from .serializers import MusicSerializer, MusicListSerializer , CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from importlib.abc import ResourceReader


@api_view(["GET", "POST"])
def music_list(request):
    if request.method == "GET":
        # 리스트 조회
        musics = Music.objects.all()
        serializer = MusicListSerializer(musics, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        # Music 생성
        serializer = MusicSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def music_detail(request, music_pk):
    music = get_object_or_404(Music, pk=music_pk)

    if request.method == "GET":
        serializer = MusicSerializer(music)
        return Response(serializer.data)
    elif request.method == "PUT":
        serializer = MusicSerializer(music, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        music.delete()
        data = {"delete": f"데이터 {music_pk}번 음악이 삭제되었습니다."}
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments,many=True)
        return Response(serializer.data)

@api_view(['GET','PUT','DELETE'])
def comment_detail(request,comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CommentSerializer(comment , data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'delete' : f'댓글 {comment_pk}번이 삭제되었습니다.'
        }
        return Response(data,status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def comment_create(request,music_pk):
    # music = Music.objects.get(pk=music_pk)
    music = get_object_or_404(Music,pk=music_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(music=music)
        return Response(serializer.data,status=status.HTTP_201_CREATED)
