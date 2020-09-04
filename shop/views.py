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
        form_data = ProductForm(request.POST, request.FILES)

        if form_data.is_valid():

            # image = request.FILES['image']
            product = Product(**form_data.cleaned_data)
            # product.iamge = image
            product.save()
            
            return redirect('input-product')
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
