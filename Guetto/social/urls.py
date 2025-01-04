from django.urls import path
from .views import PostListView, PostDetailView, AddLike
from .models import Post
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
        path('', PostListView.as_view(), name='post-list'),
        path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
        path('post/<int:pk>/like', AddLike.as_view(), name='like'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)