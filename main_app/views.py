from django.shortcuts import render
from django.views.generic import ListView, DetailView

from main_app.models import Product, Category


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
