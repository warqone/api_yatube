from django.shortcuts import get_object_or_404
from rest_framework import viewsets

from posts.models import Comment, Group, Post
from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_post(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, pk=post_id)
        return post

    def get_queryset(self):
        post = self.get_post()
        return Comment.objects.filter(post=post)

    def perform_create(self, serializer):
        post = self.get_post()
        serializer.save(post=post, author=self.request.user)
