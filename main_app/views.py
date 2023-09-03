from django.shortcuts import render

from main_app.models import Product, Category


def home(request):
    home = Category.objects.all()
    context = {
        'object_list': home,
        'title': 'Главная'
    }
    return render(request, "main_app/home.html", context)


def product_page(request):
    product_page = Product.objects.all()
    context = {
        'object_list': product_page
    }
    return render(request, "main_app/product_page.html", context)


def contact(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main_app/contacts.html', context)
