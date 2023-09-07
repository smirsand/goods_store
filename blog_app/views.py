from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from blog_app.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_app/blog_app_form.html'
    fields = ('header', 'content', 'slug',)
    success_url = reverse_lazy('main_app:home')


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_app/blog_app_list.html'


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_app/blog_app_detail.html'
