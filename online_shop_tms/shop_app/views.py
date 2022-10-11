from __future__ import unicode_literals
from django.shortcuts import render, get_list_or_404, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category, Discount, ProductItem
from .serializers import CategoriesSerializer


class CategoriesView(APIView):

    def get(self, request):
        categories = get_list_or_404(Category)
        serializer = CategoriesSerializer(categories, many=True)
        return Response(serializer.data, status=200)