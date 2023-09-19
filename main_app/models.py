from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Category(models.Model):
    name_category = models.CharField(max_length=100, verbose_name='наименование категории')
    description_category = models.TextField(verbose_name='описание категории', **NULLABLE)

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='наименование продукта')
    description = models.TextField(verbose_name='описание продукта', **NULLABLE)
    image = models.ImageField(upload_to='image/', verbose_name='изображение', **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='цена продукта')
    date_of_creation = models.DateTimeField(**NULLABLE, verbose_name='Дата создания')
    date_of_change = models.DateTimeField(**NULLABLE, verbose_name='Дата изменения')

    def __str__(self):
        return f'{self.product_name}, {self.price}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ('product_name',)


class Version(models.Model):
    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    version_number = models.TextField(verbose_name='номер версии')
    version_name = models.TextField(verbose_name='название версии')
    version_flag = models.BooleanField(verbose_name='признак текущей версии')

    def __str__(self):
        return f'{self.product}, {self.version_number}, {self.version_name}, {self.version_flag}'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
        ordering = ('product',)
