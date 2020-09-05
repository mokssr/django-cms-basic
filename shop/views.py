from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.conf import settings
from django.urls import reverse

from .models import Product
from .forms import ProductForm

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {
        'product_list':products
    })

def input_product(request):
    if request.method == 'POST':
        form_data = ProductForm(request.POST or None, request.FILES or None)

        if form_data.is_valid():

            image = form_data.cleaned_data.get('image')
            product = Product(**form_data.cleaned_data)
            product.image = image if image is not None else settings.DEFAULT_PRODUCT_IMAGE
            product.save()
            
            return redirect('input_product')
        else:
            return form_data.errors

    else:
        products = Product.objects.all()
        form = ProductForm()

    return render(request, 'input_product.html', {
        'product_list':products,
        'form':form
    })

def product_detail(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        return render(request, 'product_details.html', {
            'product':product,
            'product_image_static':'images/{}'.format(product.image)
        })
    except Product.DoesNotExist:
        return redirect('admin/products')

def buy_product(request, product_slug):
    try:
        product = Product.objects.get(slug=product_slug)
        return render(request, 'buy_product.html', {
            'product':product,
            'product_image_static':'images/{}'.format(product.image)
        })
    except Product.DoesNotExist:
        return redirect(reverse('home'))