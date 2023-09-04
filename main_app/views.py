from django.shortcuts import render

from main_app.models import Product, Category


def home(request):
    context = {
        'object_list': Category.objects.all(),
        'title': 'Главная'
    }
    return render(request, "main_app/home.html", context)


def product_page(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Продукты'
    }
    return render(request, "main_app/product_page.html", context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main_app/contacts.html', context)


def card_product(request, pk):
    category_item = Product.objects.get(pk=pk)
    context = {
        'object_list': Product.objects.filter(category=pk),
        'title': f'Карточка товара - {category_item.product_name}',
        'description': category_item.description,
        'price': category_item.price,
        'image': category_item.image
    }

    return render(request, 'main_app/card_product.html', context)
