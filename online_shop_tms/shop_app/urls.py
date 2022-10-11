from django.urls import re_path
from .views import CategoriesView

urlpatterns = [
    re_path(r'^categories/', CategoriesView.as_view()),

]