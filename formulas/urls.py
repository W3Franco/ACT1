from django.urls import path
from .views import input_formula

urlpatterns = [
    path('', input_formula, name='input_formula'),
]