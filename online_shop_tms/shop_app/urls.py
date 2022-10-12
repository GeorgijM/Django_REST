from django.urls import re_path
from .views import CategoriesView, DiscountView, PromocodeView, ProductItemView

urlpatterns = [
    re_path(r'^categories/', CategoriesView.as_view()),
    re_path(r'^discounts/', DiscountView.as_view()),
    re_path(r'^promocodes/', PromocodeView.as_view()),
    re_path(r'^products/', ProductItemView.as_view()),

]
