from django.urls import path

from blog_app.apps import BlogConfig
from blog_app.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('list/', BlogListView.as_view(), name='list'),
    path('view/<slug:slug>/', BlogDetailView.as_view(), name='view'),
    path('edit/<slug:slug>/', BlogUpdateView.as_view(), name='edit'),
    path('delete/<slug:slug>/', BlogDeleteView.as_view(), name='delete'),
]
