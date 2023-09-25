from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import inlineformset_factory
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView


from main_app.forms import ProductForm, VersionForm
from main_app.models import Category, Product, Version


class CategoryListView(ListView):
    """Контроллер списка категорий продуктов."""

    model = Category
    template_name = 'main_app/home.html'
    extra_context = {'title': 'Главная'}


class ProductListView(ListView):
    """Контроллер списка продуктов."""

    model = Product
    template_name = 'main_app/product_page.html'
    extra_context = {'title': 'Продукты'}


def contact(request):
    """Контроллер контактов."""
    context = {
        'title': 'Контакты'
    }
    return render(request, 'main_app/contacts.html', context)


class CardDetailView(DetailView):
    """Контроллер удаления карточки товара."""

    model = Product
    template_name = 'main_app/card_product.html'
    extra_context = {'title': 'Карточка товара'}


class ProductCreateView(LoginRequiredMixin, CreateView):
    """Контроллер создания товара."""

    model = Product
    form_class = ProductForm
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('main_app:product_page')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    """Контроллер редактирования товара."""

    model = Product
    form_class = ProductForm
    template_name = 'main_app/product_form.html'
    success_url = reverse_lazy('main_app:product_page')

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        VersionFormset = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = VersionFormset(self.request.POST, instance=self.object)
        else:
            formset = VersionFormset(instance=self.object)

        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
            form.instance.user = self.request.user
            formset.instance = self.object
            formset.save()
        return super().form_valid(form)
