from django.shortcuts import render
from django.views import View
from .models import Post
from .forms import PostForm

class PostListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all().order_by('-created_on')
        form = PostForm()

        context = {
                'post_list' : posts,
                'form' : form,
            }

        return render(request, 'social/post_list.html', context)