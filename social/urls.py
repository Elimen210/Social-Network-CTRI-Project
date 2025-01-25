from django.urls import path
from .views import PostListView, PostDetailView, AddLike, AddCommentLike, CommentReplyView
from .models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', PostListView.as_view(), name='post-list'),
        path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
        path('post/<int:post_pk>/comment/<int:pk>/reply', CommentReplyView.as_view(), name ='comment-reply'),
        path('post/<int:pk>/like', AddLike.as_view(), name='like'),
        path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    ] 