from django.urls import path
from .views import PostListView, PostDetailView, AddLike, AddCommentLike
from .models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', PostListView.as_view(), name='post-list'),
        path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
        path('post/<int:pk>/like', AddLike.as_view(), name='like'),
        path('post/<int:post_pk>/comment/<int:pk>/like', AddCommentLike.as_view(), name='comment-like'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)