from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('admin/products', views.input_product, name="input_product"),
    path('admin/products/<slug:product_slug>', views.product_detail, name="product_detail"),
    path('product/<slug:product_slug>/buy', views.buy_product, name="buy_product")
]
