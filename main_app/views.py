from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from main_app.forms import ProductForm
from main_app.models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'main_app/home.html'
    extra_context = {'title': 'Главная'}


class ProductListView(ListView):
    model = Product
    template_name = 'main_app/product_page.html'
    extra_context = {'title': 'Продукты'}


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main_app/contacts.html', context)


class CardDetailView(DetailView):
    model = Product
    template_name = 'main_app/card_product.html'
    extra_context = {'title': 'Карточка товара'}


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('main_app:product_page')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('main_app:product_page')
