from django.core.validators import MinValueValidator
from django.db import models
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy



class Product(models.Model):
    name = models.CharField(max_length=50,
        unique=True,
        verbose_name=pgettext_lazy('help text for MyModel model', 'Enter product name'))
    description = models.TextField()
    quantity = models.IntegerField(
        validators=[MinValueValidator(0)],
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name=pgettext_lazy('help text for MyModel model', 'Enter product category')
    )
    price = models.FloatField(
        validators=[MinValueValidator(0.0)],
    )

    def __str__(self):
        return f'{self.name.title()}: {self.description[:100]}'

    def get_absolute_url(self):
        return f'/products/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs) # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'product-{self.pk}')

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, help_text=_('category name'))

    def __str__(self):
        return self.name.title()


class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add=True)
    time_out = models.DateTimeField(null=True)
    cost = models.FloatField(default=0.0)
    take_away = models.BooleanField(default=False)
    complete = models.BooleanField(default=False)

    products = models.ManyToManyField(Product, through='ProductOrder')


class ProductOrder(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amount = models.IntegerField(default=1)
