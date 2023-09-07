from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blog_app.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_app/blog_app_form.html'
    fields = ('header', 'content', 'slug',)
    success_url = reverse_lazy('main_app:home')


class BlogUpdateView(UpdateView):
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


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_app/blog_app_confirm_delete.html'
    success_url = reverse_lazy('blog_app:list')
