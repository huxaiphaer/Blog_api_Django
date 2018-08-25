""""
add render
"""

from rest_framework import generics
from .models import Post
from .serializers import PostSerializer

# Create your views here.

class PostList(generics.ListAPIView):
    """
    post list
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    post detail
    """
    queryset = Post.objects.all()
    serializer_class = PostSerializer
