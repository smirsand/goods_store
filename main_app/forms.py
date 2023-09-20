from django import forms

from main_app.models import Product, Version


class ProductForm(forms.ModelForm):
    """Форма создания и редактирования карточки продукта."""
    class Meta:
        model = Product
        # fields = ('product_name', 'description', 'price', 'category', 'image')
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        cleaned_data = self.cleaned_data['product_name']

        words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

        for word in words:
            if word == cleaned_data:
                raise forms.ValidationError('Запрещенное слово! Выберите другое слово.')
        return cleaned_data


class VersionForm(forms.ModelForm):
    """Форма версии продукта."""

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
