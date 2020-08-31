from django.http import HttpResponse
from django.shortcuts import render, redirect

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
        form_data = ProductForm(request.POST)

        if form_data.is_valid():

            product = Product(**form_data.cleaned_data)
            product.save()
            
            return redirect('input-product')

    else:
        products = Product.objects.all()
        form = ProductForm()

    return render(request, 'input_product.html', {
        'product_list':products,
        'form':form
    })