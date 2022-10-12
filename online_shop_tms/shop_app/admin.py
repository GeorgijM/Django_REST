from __future__ import unicode_literals
from django.contrib import admin
from .models import Category, Discount, ProductItem, Promocode


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent')


class ProductItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', "count_on_stock", 'category')
    search_fields = ('name', 'category__name')
    list_select_related = ('category',)


class PromocodeAdmin(admin.ModelAdmin):
    list_display = ('name', 'percent', 'expire')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(ProductItem, ProductItemAdmin)
admin.site.register(Promocode, PromocodeAdmin)
