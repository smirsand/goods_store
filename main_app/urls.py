from django.urls import path

from main_app.views import contact, home, product_page
from main_app.apps import MainAppConfig

app_name = MainAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('product_page/', product_page, name='product_page'),
    path('contacts/', contact, name='contact')
]
