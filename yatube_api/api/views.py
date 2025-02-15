from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import PostSerializer, GroupSerializer
from posts.models import Post, Group


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def update(self, request, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().update(request, **kwargs)

    def partial_update(self, request, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().partial_update(request, **kwargs)

    def destroy(self, request, **kwargs):
        post = self.get_object()
        if post.author != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        return super().destroy(request, **kwargs)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
