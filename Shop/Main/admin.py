from django.contrib import admin

from Main.models import Product, Cart


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'price', 'image', 'slug']
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_per_page = 20
    list_editable = ('price',)


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    fields = ['user', 'product']
    list_display = ['id', 'user', 'product']
    list_per_page = 20
