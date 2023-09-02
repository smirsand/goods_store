from django.shortcuts import render


def product_page(request):
    return render(request, 'main_app/product_page.html')
