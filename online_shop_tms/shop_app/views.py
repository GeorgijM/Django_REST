from __future__ import unicode_literals
from django.shortcuts import render, get_list_or_404, get_object_or_404
# from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Category, Discount, ProductItem, Promocode
from .serializers import CategoriesSerializer, DiscountSerializer, PromocodeSerializer, ProductItemSerialer


class CategoriesView(ListAPIView):
    queryset = get_list_or_404(Category)
    serializer_class = CategoriesSerializer

    # alternative longest way to serialize from 'APIView' instead of 'ListAPIView'
    # def get(self, request):
    #     categories = get_list_or_404(Category)
    #     serializer = CategoriesSerializer(categories, many=True)
    #     return Response(serializer.data, status=200)


class DiscountView(ListAPIView):
    queryset = get_list_or_404(Discount)
    serializer_class = DiscountSerializer


class PromocodeView(ListAPIView):
    queryset = get_list_or_404(Promocode)
    serializer_class = PromocodeSerializer


class ProductItemView(ListAPIView):
    queryset = get_list_or_404(ProductItem)
    serializer_class = ProductItemSerialer
