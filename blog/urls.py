from django.urls import path
from .views import CreateBlogPostView
from .views import CreateCommentView
from .views import ListBlogPostsView
from .views import ListCommentsView
from .views import UpdateBlogPostView

urlpatterns = [
    path('create/', CreateBlogPostView.as_view(), name='create-blog-post'),
    path('create-comment/<int:blog_post_id>/', CreateCommentView.as_view(), name='create-comment'),
    path('list-blog-posts/', ListBlogPostsView.as_view(), name='list-blog-posts'),
    path('list-comments/<int:blog_post_id>/', ListCommentsView.as_view(), name='list-comments'),
    path('update-blog-post/<int:pk>/', UpdateBlogPostView.as_view(), name='update-blog-post'),
    # Other URLs
]
