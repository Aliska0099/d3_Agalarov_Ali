from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Author, Category, Post, Comment



class NewsList(ListView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'news'
    queryset = Post.objects.order_by('-dateCreation')
    paginate_by = 2


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['value1'] = "топово"
        return context




class NewsDetail(DetailView):
    model = Post
    template_name = 'post.html'
    context_object_name = 'post'