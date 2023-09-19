from django.urls import path

from main_app.views import contact, CategoryListView, ProductListView, CardDetailView, ProductCreateView, \
    ProductUpdateView

from main_app.apps import MainAppConfig

app_name = MainAppConfig.name

urlpatterns = [
    path('', CategoryListView.as_view(), name='home'),
    path('product_page/', ProductListView.as_view(), name='product_page'),
    path('contacts/', contact, name='contact'),
    path('<int:pk>/card_product/', CardDetailView.as_view(), name='card_product'),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
]
