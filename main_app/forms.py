from django import forms

from main_app.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product_name', 'description', 'price', 'category', 'image')

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word == cleaned_data:
                raise forms.ValidationError('Запрещенное слово! Выберите другое слово.')

        return cleaned_data
