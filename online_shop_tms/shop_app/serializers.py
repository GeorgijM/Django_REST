from rest_framework import serializers

from .models import Category, Discount, Promocode, ProductItem


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = '__all__'


class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = '__all__'


class ProductItemSerialer(serializers.ModelSerializer):
    #serializer for serializer since we have foreingkey in model for this fields (without
    #only 'id' will be shown
    category = CategoriesSerializer()
    discount = CategoriesSerializer()

    class Meta:
        model = ProductItem
        fields = ('id', 'name', 'description', 'count_on_stock', 'price', 'category', 'discount')
