from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from pytils import translit


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name='Product', unique=True)
    description = models.TextField(verbose_name='Description')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price')
    image = models.ImageField(upload_to='uploads/%Y/%m/%d', blank=True, verbose_name='Image')
    slug = models.SlugField(verbose_name='Slug', max_length=255, unique=True, db_index=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(translit.slugify(self.name) + '-slug')
        super(Product, self).save(force_insert, force_update, using, update_fields)

    def get_absolute_url(self):
        return reverse('product', kwargs={'product_slug': self.slug})


class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='User')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Product')

    objects = models.Manager()

    def __str__(self):
        return self.user.username
