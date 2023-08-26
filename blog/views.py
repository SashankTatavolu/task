from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer
from .models import Comment
from .serializers import CommentSerializer


from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from rest_framework.generics import ListAPIView

from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated


class CreateBlogPostView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

class CreateCommentView(APIView):
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]    

class CreateBlogPostView(APIView):
    def post(self, request):
        serializer = BlogPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user)  # Assuming user is authenticated
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CreateCommentView(APIView):
    def post(self, request, blog_post_id):
        blog_post = BlogPost.objects.get(pk=blog_post_id)
        serializer = CommentSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(author=request.user, blog_post=blog_post)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListBlogPostsView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

class ListCommentsView(ListAPIView):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        blog_post_id = self.kwargs['blog_post_id']
        return Comment.objects.filter(blog_post_id=blog_post_id)


class UpdateBlogPostView(RetrieveUpdateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.save()  # This will update the blog post's 'updated_at' field
