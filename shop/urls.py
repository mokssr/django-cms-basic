from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('admin/products', views.input_product, name="input-product")
]
