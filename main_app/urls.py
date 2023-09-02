from django.urls import path

from main_app.views import product_page

urlpatterns = [
    path('', product_page)
]
