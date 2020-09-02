from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label='Nama Produk', max_length=120, required=True)
    slug = forms.SlugField(label='Link produk', max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, label='Deskripsi Produk')
    price = forms.IntegerField(label="Harga Produk", min_value=1000)
    stock = forms.IntegerField(label="Jumlah Stok", min_value=0)
    image = forms.ImageField(label="Foto produk")