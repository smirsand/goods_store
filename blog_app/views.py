from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog_app.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    template_name = 'blog_app/blog_app_form.html'
    fields = ('header', 'content',)
    success_url = reverse_lazy('blog_app:list')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()

        return super().form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'blog_app/blog_app_form.html'
    fields = ('header', 'content',)

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = slugify(new_mat.header)
            new_mat.save()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_app:view', args=[self.kwargs.get('slug')])


class BlogListView(ListView):
    model = Blog
    template_name = 'blog_app/blog_app_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(sign_of_publication=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog_app/blog_app_detail.html'

    def get_object(self, qeryset=None):
        self.object = super().get_object(qeryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog_app/blog_app_confirm_delete.html'
    success_url = reverse_lazy('blog_app:list')
